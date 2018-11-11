from rest_framework import generics, status, filters, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.product.api.serializers import ProductSerializer, \
    ProductDetailSerializer, CreateProductSerializer, CRUDProductSerializer
from apps.product.models import Product, ProductDetail
from apps.product.paginations import TenPagination


class ListProductAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = TenPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class CreateProductAPIView(generics.CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        return serializer.save()


class GetUpdateDeleteProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CRUDProductSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        id = self.kwargs.get('pk')
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            product = None
        return product

    def retrieve(self, request, *args, **kwargs):
        object = self.get_object()
        if object:
            serializer = ProductSerializer(object, context={
                'request': request})
            return Response(serializer.data)
        else:
            return Response(
                {'details': ['Product does not exist']},
                status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        updt = self.perform_update(serializer)
        serializer = ProductSerializer(updt, context={'request': request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def perform_update(self, serializer):
        return serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            id = self.kwargs.get('pk')
            product = Product.objects.get(id=id)
            if product:
                product.delete()
                return Response({'details': ['Product deleted!']},
                        status=status.HTTP_200_OK)
        except:
            return Response({'details': ['Product not found!']},
                        status=status.HTTP_400_BAD_REQUEST)


class PutProductAPIView(viewsets.ModelViewSet):
    """Just update some fields with 'PUT'"""
    queryset = Product.objects.filter(is_active=True)
    serializer_class = CRUDProductSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        if self.request.method == 'PUT':
            product = Product.objects.filter(id=self.kwargs.get('pk')).first()
            if product:
                return product
            else:
                return Product(id=self.kwargs.get('pk'))
        else:
            return super(PutProductAPIView, self).get_object()

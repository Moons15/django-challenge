from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from apps.account.models import User
from rest_framework import serializers


class CreateSuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name',)
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'],
                                   is_superuser=True)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        error_messages={"blank": "This field is required"})
    password = serializers.CharField(
        error_messages={"blank": "This field is required"})

    def validate(self, attrs):
        self.user_cache = authenticate(email=attrs["email"],
                                       password=attrs["password"])
        if not self.user_cache:
            raise serializers.ValidationError({'details': ['Invalid login']})
        else:
            return attrs

    def get_user(self):
        return self.user_cache

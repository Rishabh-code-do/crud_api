from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from .models import Box

User = get_user_model()


class BoxSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    last_updated = serializers.SerializerMethodField()

    class Meta:
        model = Box
        fields = '__all__'

    def get_created_by(self, obj):
        user = self.context['request'].user
        return str(obj.created_by) if user.is_staff else None

    def get_last_updated(self, obj):
        user = self.context['request'].user
        return obj.last_updated if user.is_staff else None

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email','is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_staff=validated_data.get('is_staff', False)
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)


    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    data['user'] = user
                    data['is_staff'] = user.is_staff
                else:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError("Incorrect username or password.")
        else:
            raise serializers.ValidationError("Must provide both username and password.")

        return data
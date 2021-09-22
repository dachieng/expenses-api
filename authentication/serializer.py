from django.db.models import fields
from django.db.models.fields import EmailField
from rest_framework import serializers
from authentication.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6, max_length=56, write_only=True)

    def validate(self, attrs):

        username = attrs.get('username', '')

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {'email': 'email already exists'})

        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError(
                {'username': 'username already exists'})

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should contain only alphanumeric characters')

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

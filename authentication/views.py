from authentication.models import User
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from authentication.serializer import UserRegistrationSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistration(ListCreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def list(self, request):
        users = User.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data

            user = User.objects.get(email=user_data['email'])

            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class RegisterView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Something went wrong while registering user"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({
                'data':{},
                'message': "User created successfully"
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data      
            #print(data)
            serializer = LoginSerializer(data = data)

            a = serializer.is_valid();
            print(a)
            if not a:
                return Response({
                    'data': serializer.errors,
                    'message': "Invalid credentials"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            print('p')
            response_data = serializer.get_jwt_token(serializer.validated_data)
            print(response_data)
            print('f')

            return Response(
                response_data, status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
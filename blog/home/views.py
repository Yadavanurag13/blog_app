from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from django.db.models import Q

class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def get(self, request):
        try:
            search = request.GET.get('search', '')

            # Filter blogs by user and apply search filter if exists
            blogs = Blog.objects.filter(user=request.user)

            if search:
                blogs = blogs.filter(Q(title__icontains=search) | Q(content__icontains=search))

            # Serialize the blogs
            serializer = BlogSerializer(blogs, many=True)

            return Response({
                'data': serializer.data,
                'message': "Blog fetched successfully"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong in try block'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        try:
            data = request.data;

            data['user'] = request.user.id
            #print(request.user)

            serializer = BlogSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': "Something went wrong while creating blog"
                }, status=status.HTTP_400_BAD_REQUEST)
            

            serializer.save()
            return Response({
                'data':serializer.data,
                'message': "Blog created successfully"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
            
                
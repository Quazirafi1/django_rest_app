from .models import Blog, Category
from .serializer import BlogSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

#Viewsets
# class BlogViewSet(viewsets.ViewSet):
#     def list(self, request):
#         query_set = Blog.objects.filter(is_public = True)
#         serializer = BlogSerializer(query_set, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         query_set = Blog.objects.filter(is_public = True)
#         blog_list = get_object_or_404(query_set, pk=pk)
#         serializer = BlogSerializer(blog_list)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = BlogSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk=None):
#         blog = get_object_or_404(Blog, pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         blog.delete()
#         return Response({"Message": "Your Blog Has Been Deleted"},status.HTTP_204_NO_CONTENT)

#ModelViewset
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(is_public = True)
    serializer_class = BlogSerializer
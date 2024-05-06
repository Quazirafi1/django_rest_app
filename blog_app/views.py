from .models import Blog, Category
from .serializer import BlogSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class CategoryListView(APIView):
    def get(self, request):
        all_category = Category.objects.all()
        serializers = CategorySerializer(all_category, many=True)
        return Response(serializers.data)

class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializers = CategorySerializer(category)
        return Response(serializers.data)


#GET, POST
class BlogListView(APIView):
    def get(self, request):
        all_blogs = Blog.objects.all()
        serializer = BlogSerializer(all_blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET, PUT, DELETE
class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_200_OK)
    
# @api_view(['GET', 'POST'])
# def blog(request):
#     if request.method == 'GET':
#         all_blogs = Blog.objects.all()
#         serializer = BlogSerializer(all_blogs, many=True)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def blog_detail(request, pk):
#     if request.method == 'GET':
#         blog = Blog.objects.get(pk=pk)
#         serializer = BlogSerializer(blog)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         blog = Blog.objects.get(pk=pk)
#         serializer = BlogSerializer(blog, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         blog = Blog.objects.get(pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_200_OK)
        

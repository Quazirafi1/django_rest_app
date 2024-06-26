from .models import Blog, Category, BlogComment
from .serializer import BlogSerializer, CategorySerializer, BlogCommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly


class CategoryListCreateView(generics.ListCreateAPIView):
    
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True, context = {'request': request})
        
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Category Found"}, status=status.HTTP_204_NO_CONTENT)
    
    
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Blogs Found"}, status=status.HTTP_204_NO_CONTENT)
        
    
    
class BlogListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.filter(is_public=True)
    serializer_class = BlogSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many = True, context = {'request': request})
        
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Blogs Found"}, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Blog.objects.filter(is_public=True)
    serializer_class = BlogSerializer
    lookup_field = 'pk'
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        if instance:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Blogs Found"}, status=status.HTTP_204_NO_CONTENT)
        

class BlogCommentListCreateView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Fetch id from URL
        # Get comments related to the blog
        blog_id = self.kwargs.get('blog_id')
        return BlogComment.objects.filter(blog_id=blog_id)
    
    def perform_create(self, serializer):
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(Blog, id=blog_id)
        
        # limiting one comment for a single user in a post
        if BlogComment.objects.filter(blog=blog, author=self.request.user).exists():
           raise serializers.ValidationError({'Message': 'You already posted a comment on this blog'})
        
        serializer.save(author=self.request.user, blog=blog) 
        

class BlogCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    
    def get_object(self):
        comment_id = self.kwargs.get("comment_id")
        comment = get_object_or_404(BlogComment, id = comment_id)
        
        blog_id = self.kwargs.get("blog_id")
        if comment.blog.id != blog_id:
            raise serializers.ValidationError({"Message": "Comment is not related to the requested blog!"}, status=status.HTTP_401_UNAUTHORIZED)
        return comment 
    
    def put(self, request, *args, **kwargs):
        comment = self.get_object()
        
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "Not authorized to edit!"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *kwargs, **args) 
    
    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        
        if comment.author != request.user:
            raise serializers.ValidationError({"Message": "Not authorized to edit!"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *kwargs, **args) 
        
from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog
# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    
    data = {
        "Blogs": list(blogs.values())
    }
    
    return JsonResponse(data)

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    
    data = {
        "name": blog.name,
        "description": blog.description, 
        "slug": blog.slug,
    }
    
    return JsonResponse(data)
    

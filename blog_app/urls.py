from django.urls import path, include
from . import views
from rest_framework import routers

# for viewsets
# router = routers.DefaultRouter()
# router.register(r'blogs', views.BlogViewSet, basename="blogs")

urlpatterns = [
    # for viewsets 
    # path('', include(router.urls)) 
    path('blog_list/', views.BlogListCreateView.as_view(), name='blog-list'),
    path('blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('category_list/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('category_detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('blog_comment_list/<int:blog_id>/', views.BlogCommentListCreateView.as_view(), name='blog-comment-list'),
]

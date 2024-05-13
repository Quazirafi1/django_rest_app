from django.urls import path
from . import views

urlpatterns = [
    # path('blog/', views.blog, name="blog"),
    # path('blog_detail/<int:pk>/', views.blog_detail, name="blog_detail"),

    #class based view urls
    path('blog/', views.BlogListView.as_view(), name="blog"),
    path('blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    
    #category url
    path('category_list/', views.CategoryListView.as_view(), name="category_list"), 
    path('category_detail/<int:pk>/', views.CategoryDetailView.as_view(), name="category-detail"),      
    
    #generic view 
    path('blog_list_generic/', views.BlogListGenericView.as_view(), name="blog_list_generic"),     
    path('blog_detail_generic/<str:slug>', views.BlogDetailGeneric.as_view(), name="blog_detail_generic"),     
    
    #api view
    path('blog_create_api_view/', views.BlogCraeteView.as_view(), name="blog_create_api_view"),     
    path('blog_list_api_view/', views.BlogListView.as_view(), name="blog_list_api_view"),     
    # path('blog_retrieve_api_view/<int:pk>/', views.BlogRetrieveView.as_view(), name="blog_list_api_view"),     
    path('blog_retrieve_api_view/<str:slug>/', views.BlogRetrieveView.as_view(), name="blog_retrieve_api_view"),     
    path('blog_destroy_api_view/<int:pk>/', views.BlogDestroyView.as_view(), name="blog_destroy_api_view"),     
    path('blog_retrieve_update_destroy_api_view/<int:pk>/', views.BlogRetrieveUpdateDestroyView.as_view(), name="blog_retrieve_update_destroy_api_view"),     
    path('blog_list_create_api_view/', views.BlogListCreateView.as_view(), name="blog_list_create_api_view"),     

]

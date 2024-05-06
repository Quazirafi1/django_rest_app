from rest_framework import serializers
from .models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    #must be same as related name present in the model
    category = BlogSerializer(many=True, read_only = True)
    
    class Meta:
        model = Category
        exclude = ["id"]
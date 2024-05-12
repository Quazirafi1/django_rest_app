from rest_framework import serializers
from .models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.CharField()
    category = serializers.HyperlinkedRelatedField(many=True, read_only = True, view_name="blog_detail") 
 
    class Meta:
        model = Category
        fields = '__all__'
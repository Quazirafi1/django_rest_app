from rest_framework import serializers
from .models import Blog, Category, BlogComment
from django.urls import reverse

class BlogCommentSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField(read_only = True)
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = BlogComment
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    # nesting serializers to show related comments as well
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = "__all__"
    
    def get_comments(self, obj):
        # show only 3 comments
        comments = BlogComment.objects.filter(blog = obj)[:3]
        request = self.context.get('request')
        return {
            "comments" : BlogCommentSerializer(comments, many=True).data, 
            # if there are more than 3 comments for the post
            # give link to all comments
            "all_comment_link": request.build_absolute_uri(reverse('blog-comment-list', kwargs= {'blog_id': obj.id}))   
        }       
        
class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True) 
 
    class Meta:
        model = Category
        fields = "__all__"
        

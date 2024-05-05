from rest_framework import serializers
from .models import Blog
class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =  True)
    name = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    post_date = serializers.DateField()
    is_public = serializers.BooleanField()
    slug = serializers.CharField()
    
    #for post requests
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
    
    #for put, patches
    def update(self, instance, validated_data):
        # validated_data.get('name', instance.name): This part is using the get() method on a dictionary-like object called validated_data. 
        # It tries to retrieve the value associated with the key 'name' from validated_data. If the key 'name' exists in validated_data, it returns the corresponding value.
        # If the key doesn't exist, it returns instance.name (old data).
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.post_date = validated_data.get('post_date', instance.post_date)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.slug = validated_data.get('slug', instance.slug)
        
        instance.save()
        return instance
    

from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify
class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    post_date = models.DateField(default=date.today)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.name + " " + str(self.author)
    
    # *args allows you to pass a variable number of positional arguments to a function, 
    # and **kwargs allows you to pass a variable number of keyword arguments
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.post_date))
        # This line calls the save method of the parent class (in this case, models.Model) using super(). 
        # It passes any additional positional (*args) or keyword (**kwargs) arguments to the parent's save method. 
        # This ensures that the normal save behavior of the Model class is preserved.
        return super().save(*args, **kwargs)
    
class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.blog)
    

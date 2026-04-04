from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPost(models.Model):
    STATUS_CHOICES = [
        ("DRAFT", 'Draft'),
        ("PUBLISHED", 'Published')
    ]
    
    
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")
    # image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
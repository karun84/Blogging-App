from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    designation=models.CharField(max_length=100,null=True,blank=True)
    education=models.CharField(max_length=300,blank=True,null=True)
    profileimage=models.ImageField(upload_to='images',blank=True,default='avatar.png')
    bio=models.CharField(max_length=600,blank=True)
    
    slug=models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super().save(*args, **kwargs)
    
    
class Category(models.Model):
    category=models.CharField(max_length=100,null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.category
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super().save(*args, **kwargs)
    
class Blog(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=500)
    author=models.ForeignKey(Profile,on_delete=models.CASCADE)
    body=RichTextField()
    tags=models.TextField(blank=True)
    image1=models.ImageField(upload_to='image',blank=True,null=True,default="default-blog.png")
    date=models.DateField(auto_now_add=True)
    upvote=models.ManyToManyField(User,symmetrical=False,blank=True,related_name="likes")
    downvote=models.ManyToManyField(User,symmetrical=False,blank=True,related_name="dislikes")
    
    slug=models.SlugField(max_length=250,null=True,blank=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)  
    
class Comment(models.Model):
    commenter=models.ForeignKey(Profile,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.CharField(max_length=800)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.blog.title)
    
    
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget


class UserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"input100",'type':"text",'name':"username",'placeholder':"username"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':"input100",'type':"email",'name':"email",'placeholder':"email"}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'class':"input100", 'type':"password",'name':"password1",'placeholder':"Password"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'class':"input100",'type':"password",'name':"password2",'placeholder':"Confirm password"}))
    
    class Meta:
        model=User
        fields=['username','email']

class BlogForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'type':"text"}))
    category=forms.CharField(required=False,widget=forms.TextInput(attrs={'name':"category",'type':"text"}))
    tags=forms.CharField(widget=forms.TextInput(attrs={'type':"text"}))
    image1=forms.ImageField(required=False)
    body=forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=Blog
        fields=['title','body','tags','image1']
    
    
class CommentForm(forms.ModelForm):
    comment=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'placeholder':"Your comment"}))
    class Meta:
        model=Comment
        fields=['comment']
        
        
class ProfileForm(forms.ModelForm):
    author=forms.CharField(widget=forms.TextInput(attrs={'type':"text",'id':"firstname",'placeholder':"Authorname",'class':"formbold-form-input"}))
    designation=forms.CharField(widget=forms.TextInput(attrs={'type':"text",'name':"designation",'id':"lastname",'placeholder':"Designation",'class':"formbold-form-input"}))
    education=forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':"4",'id':"message",'placeholder':"Write about your education...",'class':"formbold-form-input"}))
    bio=forms.CharField(widget=forms.Textarea(attrs={'rows':"6",'id':"message",'placeholder':"Write about yourself...",'class':"formbold-form-input"}))
    profileimage=forms.ImageField(required=False,widget=forms.FileInput(attrs={'type':"file",'class':"formbold-form-input"}))
    class Meta:
        model=Profile
        fields=['author','designation','education','bio','profileimage']
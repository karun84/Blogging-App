from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


def webpage(request):
    return render(request,"webpage.html")


def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('passw')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(home)
    return render(request,'signin.html')


def register_user(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password1')
        print(form)
        print("hello")
        if form.is_valid():
            print("hello")
            form.save()
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect(createprofile)
            else:
                return redirect(login_user)
    else:
        form=UserForm()
    context={
        'form':form,
    }
    return render(request,'signup.html',context)


@login_required(login_url=login_user)
def logout_user(request):
    if request.method=="POST":
        login(request,request.user)
        return redirect(login_user)
    return render(request,'signout.html')


@login_required(login_url=login_user)
def createprofile(request):
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect(home)   
    form=ProfileForm()
    context={
        'form':form,
    }
    return render(request,"profileform.html",context)

@login_required(login_url=login_user)
def editprofile(request):
    r=Profile.objects.get(user=request.user)
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES,instance=r)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect(myprofile)   
    form=ProfileForm(instance=r)
    context={
        'form':form,
    }
    return render(request,"editprofileform.html",context)

@login_required(login_url=login_user)
def home(request):
    q=reversed(Blog.objects.all())
    l=Blog.objects.all().order_by('?')[:3]
    context={
        'blogs':q,
        'random':l,
    }
    return render(request,"home.html",context)


@login_required(login_url=login_user)
def search(request):
    search=request.GET.get('search')
    q = request.GET.get('search') if request.GET.get('search') != None else ''
        
    blog_search=Blog.objects.filter( Q(title__icontains=q) |
                                    Q(category__category__icontains=q) |
                                    Q(tags__icontains=q) 
                                    | Q(author__author__icontains=q) ).order_by('-id')
    context={
        'blogs':blog_search,
        'search':search,
    }
    return render(request,"search.html",context)


@login_required(login_url=login_user)
def myprofile(request):
    user=Profile.objects.get(user=request.user)
    blog=user.blog_set.all()
    context={
        'user':user,
        'blog':blog,
    }
    return render(request,"profile.html",context)


@login_required(login_url=login_user)
def authorprofile(request,slug):
    user=Profile.objects.get(slug=slug)
    blog=user.blog_set.all()
    context={
        'user':user,
        'blog':blog,
    }
    return render(request,"profile.html",context)


@login_required(login_url=login_user)
def blogcategory(request):
    cat=Category.objects.all()
    context={
        'category':cat,
    }
    return render(request,"category.html",context)


@login_required(login_url=login_user)
def opencategory(request,cat):
    c=Category.objects.get(slug=cat)
    blogs=Blog.objects.filter(category=c).order_by('-id')
    context={
        'blogs':blogs,
        'category':cat,
    }
    return render(request,"category-blogs.html",context)


@login_required(login_url=login_user)
def open_blog(request,slug):
    blog=Blog.objects.get(slug=slug)
    comments=blog.comment_set.all()
    user=User.objects.get(username=request.user)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            commenter=Profile.objects.get(user=request.user)
            t=form.save(commit=False)
            t.commenter=commenter
            t.blog=blog
            t.save()
    if request.method=="GET":
        action=request.GET.get('vote')
        print(action)
        if action=="upvote":
            blog.upvote.add(user)
        elif action=="undoupvote":
            blog.upvote.remove(user)
        elif action=="downvote":
            blog.downvote.add(user)
        elif action=="undodownvote":
            blog.downvote.remove(user)
    form=CommentForm()
    context={
        'blog':blog,
        'comments':comments,
        'form':form,
        'user':user,
    }
    return render(request,"open-blog.html",context)


@login_required(login_url=login_user)
def newBlog(request):
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            cat=request.POST.get('category')
            cat=cat.lower()
            Category.objects.get_or_create(category=cat)
            category=Category.objects.get(category=cat)
            a=Profile.objects.get(user=request.user)
            blog=form.save(commit=False)
            blog.author=a
            blog.category=category
            blog.save()
            return redirect(home)
            
    form=BlogForm()
    context={
        'form':form,
    }
    return render(request,"newblog.html",context)


@login_required(login_url=login_user)
def editBlog(request,id):
    r=Blog.objects.get(id=id)
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES,instance=r)
        print(form)
        if form.is_valid():
            a=Profile.objects.get(user=request.user)
            blog=form.save(commit=False)
            blog.author=a
            blog.save()
            return redirect(myprofile)
            
    form=BlogForm(instance=r)
    context={
        'form':form,
    }
    return render(request,"editblog.html",context)


@login_required(login_url=login_user)
def deleteblog(request,id):
    blog=Blog.objects.get(pk=id)
    blog.delete()
    return redirect(myprofile)


from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    path('',views.webpage,name="webpage"),
    
    path('login',views.login_user,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('register',views.register_user,name="register"),
    
    path('Home',views.home,name="home"),
    
    path('Myprofile',views.myprofile,name="myprofile"),
    
    path('Newblog',views.newBlog,name="newblog"),
    path('Editblog/<int:id>',views.editBlog,name="editblog"),
    
    path('Categories',views.blogcategory,name="category"),
    path('Category/<slug:cat>',views.opencategory,name="cat-blogs"),
    
    path('Blog/<slug:slug>',views.open_blog,name="openblog"),
    path('Author/<slug:slug>',views.authorprofile,name="authorprofile"),
    

    path('Search',views.search,name="search"),
    
    path('Delete/<int:id>',views.deleteblog,name='deleteblog'),
    
    path('createprofile',views.createprofile,name="create-profile"),
    path('test',views.editprofile,name='edit-profile'),
         
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

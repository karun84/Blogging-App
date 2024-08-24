from django.contrib import admin
from .models import Blog,Profile,Comment,Category
# Register your models here.

admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Category)

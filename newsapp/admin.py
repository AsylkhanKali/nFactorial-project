from django.contrib import admin
from .models import NewsPost, Category, Comment

# Register your models here.
admin.site.register(NewsPost)
admin.site.register(Category)
admin.site.register(Comment)

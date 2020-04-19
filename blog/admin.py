from django.contrib import admin
from .models import Category, Post, Comment


admin.site.site_header = "Food Portfolio Administration"

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

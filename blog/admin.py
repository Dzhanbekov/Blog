from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_posted', 'author']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']
    list_filter = ['date_posted']


admin.site.register(Post, PostAdmin)
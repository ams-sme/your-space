from django.contrib import admin
from feed.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('likers',)

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)

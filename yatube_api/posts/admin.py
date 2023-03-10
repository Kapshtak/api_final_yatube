from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")


class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "following")


admin.site.register(Follow, FollowAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment)

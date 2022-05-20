from django.contrib import admin

from posts.models import Comment, Group, Post, Follow

EMPTY_VD = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = EMPTY_VD


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'description',
        'title',
        'slug'
    )
    search_fields = ('description', 'title')
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = EMPTY_VD


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'created',
        'author'
    )
    search_fields = ('text',)
    list_filter = ('created', 'author')
    empty_value_display = EMPTY_VD


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user', 'following')

from django.contrib import admin
from apps.post.models import Post, PostImage,  Category, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'allow_comments',
                    'created_at', 'updated_at')
    search_fields = ('id', 'title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('category', 'author', 'created_at', 'allow_comments')
    ordering = ('-created_at', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at')
    search_fields = ('id', 'author__username', 'post__title')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at', )


def activate_images(modeladmin, request, queryset):
    updated = queryset.update(active=True)
    modeladmin.message_user(
        request, f"{updated} imágenes fueron activadas correctamente."
    )


activate_images.short_description = "Activar imágenes seleccionadas"


def deactivate_images(modeladmin, request, queryset):
    updated = queryset.update(active=False)
    modeladmin.message_user(
        request, f"{updated} imágenes fueron desactivadas correctamente."
    )


deactivate_images.short_description = "Desactivar imágenes seleccionadas"


class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'active', 'created_at')
    search_fields = ('post__id', 'post__title', 'image')
    list_filter = ('active', )

    actions = [activate_images, deactivate_images]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)

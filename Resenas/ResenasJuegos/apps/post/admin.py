from django.contrib import admin
from apps.post.models import Category, Post, PostImage

# Inline para imágenes relacionadas al post
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1   # cantidad mínima de forms vacíos para subir imágenes
    fields = ('image', 'active')


# Admin de Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at', 'amaount_comments', 'amount_favorites', 'average_score')
    list_filter = ('created_at', 'author', 'category')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}  # genera automáticamente el slug
    inlines = [PostImageInline]  # para subir imágenes desde el mismo form del post
    filter_horizontal = ('category',)  # interfaz más cómoda para categorías


# Admin de Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


# Admin de PostImage
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'active')
    list_filter = ('active',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
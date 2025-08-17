from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'score', 'approbed', 'created_at', 'updated_at')
    list_filter = ('approbed', 'score', 'created_at')
    search_fields = ('user__username', 'post__title', 'content')
    list_editable = ('approbed',)  # se debería poder aprobar/desaprobar desde la lista
    ordering = ('-created_at',)


    def approve_comments(self, request, queryset):
        updated = queryset.update(approbed=True)
        self.message_user(request, f"{updated} comentarios fueron aprobados.")
    approve_comments.short_description = "Aprobar comentarios seleccionados"

    def disapprove_comments(self, request, queryset):
        updated = queryset.update(approbed=False)
        self.message_user(request, f"{updated} comentarios fueron desaprobados.")
    disapprove_comments.short_description = "Desaprobar comentarios seleccionados"

    actions = [approve_comments, disapprove_comments]


admin.site.register(Comment, CommentAdmin)
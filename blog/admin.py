from django.contrib import admin
from .models import Category,Article,Comment,Message,Like
# Register your models here.

admin.site.register(Category)
# admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)


class CommentInline(admin.TabularInline):
    model = Comment
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("__str__","title","show_image")
    list_editable = ("title",)
    list_filter = ("created","title")
    # inlines = ('CommentInline',)

class FilterByTitle(admin.SimpleListFilter):
    title = "telegram"
    parameter_name = "title"
    def lookups(self, request, model_admin):
        return (
            ("telegram","تلگرام"),
            ("linkedin","لینکدین")
        )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter("title",contains = self.value())

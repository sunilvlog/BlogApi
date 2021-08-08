from django.contrib import admin
from api.models import ArticleName
# Register your models here.
@admin.register(ArticleName)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','descryption']
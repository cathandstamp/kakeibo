from django.contrib import admin
# Register your models here.
from .models import Category, Kakeibo

#追加
class KakeiboAdmin(admin.ModelAdmin):
    list_display=('date','category','money','memo')

admin.site.register(Category)
admin.site.register(Kakeibo,KakeiboAdmin)   
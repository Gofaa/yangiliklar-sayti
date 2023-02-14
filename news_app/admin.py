from django.contrib import admin
from .models import Category, News, ContactUs

# News modelini admin panelda ko'rsatish
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # column lar
    list_display = ['title', 'slug', 'publish_time', 'status']
    # filtrlash uchun
    list_filter = ['status', 'created_time', 'publish_time']
    # slugga o'tkazish uchun
    prepopulated_fields = {"slug": ('title',)}
    # vaqt bo'yicha iarerhoyalash
    date_hierarchy = 'publish_time'
    # qidirish uchun
    search_fields = ['title', 'body']
    # tartiblash
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(ContactUs)





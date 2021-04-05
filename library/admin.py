from django.contrib import admin

from .models import Category, App


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    pass

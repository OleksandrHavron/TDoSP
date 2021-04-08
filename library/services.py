from .models import Category, App, SubCategory


def get_all_apps():
    return App.objects.all()


def get_all_categories():
    return Category.objects.all()


def get_apps_in_subcategory(slug_subcategory):
    return SubCategory.objects.filter(slug = slug_subcategory)


def get_selected_app(slug_app):
    return App.objects.filter(slug = slug_app)
from .models import Category, App, SubCategory


def get_all_apps():
    return App.objects.all()


def get_all_categories():
    return Category.objects.all()


def get_apps_by_subcategory(slug_subcategory):
    subcategory = SubCategory.objects.get(slug=slug_subcategory)
    return App.objects.filter(subcategory=subcategory)


def get_selected_app(slug_app):
    return App.objects.filter(slug=slug_app)


def get_app_by_slug(slug):
    return App.objects.get(slug=slug)

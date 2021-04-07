from .models import Category, App


def get_all_apps():
    return App.objects.all()


def get_all_categories():
    return Category.objects.all()


def get_apps_in_subcategory(id_subcategory):
    return App.objects.filter(subcategory = id_subcategory)
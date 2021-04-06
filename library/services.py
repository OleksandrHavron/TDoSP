from .models import Category, App


def get_all_apps():
    return App.objects.all()
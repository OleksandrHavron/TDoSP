from django.shortcuts import render
from .models import Category, App
from .services import get_all_apps, get_all_categories


def home_page(request):
    return render(request, 'home_page.html')


def app_list(request):
    apps = get_all_apps()

    return render(request, 'app_list.html', {
        'apps': apps,
    })


def app_page(request):
    return render(request, 'app_page.html')


def category_list(request):
    categories = get_all_categories()

    return render(request, 'category_list.html', {
        'categories': categories
    })

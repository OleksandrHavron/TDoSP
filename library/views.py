from django.shortcuts import render
from .services import get_all_apps, get_all_categories, get_apps_by_subcategory, \
    get_app_by_slug


def home_page(request):
    page_selected = "home"
    return render(request, 'home_page.html', {
           'page_selected': page_selected,
        })


def category_list(request):
    page_selected = "category"
    categories = get_all_categories()

    return render(request, 'category_list.html', {
        'categories': categories,
        'page_selected' : page_selected,
    })


def app_list_by_subcategory(request, subcategory_slug):
    apps = get_apps_by_subcategory(subcategory_slug)

    return render(request, 'app_list.html', {
            'apps': apps,
        })


def app_page(request, app_slug):
    app = get_app_by_slug(app_slug)

    return render(request, 'app_page.html', {
        'app': app
    })

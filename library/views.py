from django.shortcuts import render
from .models import Category, App


def home_page(request):
    return render(request, 'home_page.html')


def app_list(request):
    apps = App.objects.all()

    return render(request, 'app_list.html', {
        'apps': apps,
    })


def app_page(request):
    return render(request, 'app_page.html')

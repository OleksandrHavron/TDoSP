from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def app_list(request):
    return render(request, 'app_list.html')


def app_page(request):
    return render(request, 'app_page.html')

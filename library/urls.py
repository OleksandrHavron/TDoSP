from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^app_list$', views.app_list, name='app_list'),
    url(r'^app$', views.app_page, name='app_page'),

]

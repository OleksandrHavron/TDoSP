from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^categories$', views.category_list, name='categories'),
    url(r'^app_list/(?P<subcategory_slug>[-\w]+)/$', views.app_list_by_subcategory, name='app_list'),
    url(r'^app/(?P<app_slug>[-\w]+)/$', views.app_page, name='app_page'),
    
]

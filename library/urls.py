from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^app_list$', views.app_list, name='app_list'),
    url(r'^app/$', views.app_page, name='app_page'),
    url(r'^categories$', views.category_list, name='categories'),
    url(r'^app_list/(?P<id_subcategories>\w+)/$', views.app_list_with_params, name='app_list_with_params'),
    url(r'^app/(?P<slug_app>\w+)/$', views.app_page, name='app_page_with_params'),
    
]

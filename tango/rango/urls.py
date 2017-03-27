from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$' , views.index, name = 'index'),
    url(r'^register/$', views.register, name='register'), 
    url(r'^login/$',views.user_login ,name='login'),
    url(r'^restricted/$',views.restricted,name='restricted'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^search_form/$',views.search_form,name='search_form'),
    url(r'^search/$',views.search,name='search'),
    url(r'^(?P<slug>[^\.]+)/$',views.view_post,name='view_post'),
    # ADD NEW PATTERN!
]

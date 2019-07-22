from django.urls import path
from django.contrib import admin
admin.autodiscover()

from . import views


urlpatterns = [																																																																																																																																																																																																							
    path('', views.backg, name='backg'),
    path('backg1/', views.backg1, name='backg1'),
    path('archive/', views.archive, name='archive'),
    path('backg2/', views.backg2, name='backg2'),
    path('backg8/', views.createpost, name='backg8'),
    path('backg9/', views.newaccount, name='backg9'),
    path('signup/', views.UserLogin, name='signup'),
    path('search/',views.search,name='search'),
    path('logout/',views.logout,name='logout'),

]


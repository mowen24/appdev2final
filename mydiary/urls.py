from django.urls import path

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('',views.index, name='index'),
    path('home', views.HomeView.as_view(), name='home'),
    path('entry', views.entry, name='entry')
]
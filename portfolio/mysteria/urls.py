from django.urls import path

from . import views

urlpatterns = [
    path('tools/company/', views.index, name='index'),
    path('', views.index, name='index'),
]
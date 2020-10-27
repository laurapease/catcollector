from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding')
]

from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('сreate_ar', views.create_ar, name='create_ar'),
    path('сreate_al', views.create_al, name='create_al'),
    path('сreate_s', views.create_s, name='create_s'),
    path('update/<int:id>/', views.view_edit, name="update"),
    path('view_ar', views.view_ar, name="view_ar"),
    path('view_s', views.view_s, name="view_s"),
    path('view_al', views.view_al, name="view_al"),
]

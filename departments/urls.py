from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('detail/<str:pk>/edit/', views.edit, name='edit'),
    path('new/', views.new, name='new'),
]
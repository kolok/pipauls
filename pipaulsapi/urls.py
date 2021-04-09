from django.urls import path

from . import views

app_name = 'pipaulsapi'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:product_id>/', views.detail, name='detail'),
    path('edit/<uuid:product_id>/', views.edit, name='edit'),
    path('save/<uuid:product_id>/', views.save, name='save'),
]
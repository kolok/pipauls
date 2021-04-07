from django.urls import path

from . import views

urlpatterns = [
    # ex: /pipaulsapi/
    path('', views.index, name='index'),
    # ex: /pipaulsapi/5/
    path('<int:product_id>/', views.detail, name='detail'),]
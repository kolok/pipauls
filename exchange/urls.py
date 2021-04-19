from django.urls import path

from . import views

app_name = 'exchange'
urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:product_id>/', views.detail, name='detail'),
    path('edit/<uuid:product_id>/', views.edit, name='edit'),
    path('product/<uuid:pk>/detail/', views.detail, name='product-detail'),
    path('product/<uuid:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import path

from . import views

app_name = 'exchange'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product_list, name='product-list'),
    path('product/<uuid:pk>/detail/', views.product_detail, name='product-detail'),
    path('product/<uuid:pk>/update/', views.product_update, name='product-update'),
    path('product/<uuid:pk>/delete/',
      permission_required('exchange.can_edit_product', raise_exception=True)(login_required(views.ProductDelete.as_view())),
      name='product-delete'),
    path('product/create/', views.product_create, name='product-create'),
#    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
]

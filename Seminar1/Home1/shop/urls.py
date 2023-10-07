from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('order_list/<int:client_id>/', views.order_list, name='order_list'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),
    path('product_edit/<int:product_id>/', views.product_edit, name='product_edit'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),

]

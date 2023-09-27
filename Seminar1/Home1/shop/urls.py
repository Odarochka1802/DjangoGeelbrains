from django.urls import path

from . import views
from .views import ShowProduct

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/<slug:post_slug>/', ShowProduct.as_view(), name='product'),


]

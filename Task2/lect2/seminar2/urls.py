from django.urls import path

from seminar2 import views

urlpatterns = [
    path('heads/', views.heads, name='heads')
]

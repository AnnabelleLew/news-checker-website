from django.urls import path
from . import views

# The URLs and the associated views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('articles/', views.ArticleBiasesByUserListView.as_view(), name='articles'),
    path('password/', views.change_password, name='change_password'),
]

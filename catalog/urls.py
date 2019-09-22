from django.urls import path
from . import views

# The URLs and the associated views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('download/', views.download, name='download'),
    path('firefox/', views.firefox_download, name='firefox'),
    path('chrome/', views.chrome_download, name='chrome'),
    path('add/', views.add, name='add'),
    path('articles/', views.ArticleBiasesByUserListView.as_view(), name='articles'),
    path('password/', views.change_password, name='change_password'),
]

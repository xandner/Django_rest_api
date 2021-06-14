from django.urls import path,include
from .views import ArticleView,ArticleDetailView,ArticleDetailView_slug


app_name ='blog'
urlpatterns= [
    path('',ArticleView.as_view(),name='list'),
    path('<int:pk>',ArticleDetailView.as_view(),name='detail'),
    path('<slug:slug>',ArticleDetailView_slug.as_view(),name='detail'),
    
]

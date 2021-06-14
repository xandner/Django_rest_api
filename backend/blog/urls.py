from django.urls import path,include
from .views import ArticleView


app_name ='blog'
urlpatterns= [
    path('',ArticleView.as_view(),name='list')
]
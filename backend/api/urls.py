from django.urls import path,include
from .views import ArticleListView,ArticleDetailView,UserDetailView,UserList,ArticleDetailView_slug

urlpatterns=[
    path('',ArticleListView.as_view(),name='list'),
    path('<int:pk>',ArticleDetailView.as_view(),name='detail'),
    path('users/',UserList.as_view(),name='users'),
    path('users/<int:pk>',UserDetailView.as_view(),name='users_detail'),
    path('<slug:slug>',ArticleDetailView_slug.as_view(),name='detail_slug'),
    
]
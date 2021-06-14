from django.urls import path,include
from .views import ArticleListView,ArticleDetailView,UserDetailView,UserList,ArticleDetailView_slug,RevorkeToken
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from dj_rest_auth.views import PasswordResetView


urlpatterns=[
    path('',ArticleListView.as_view(),name='list'),
    path('<int:pk>',ArticleDetailView.as_view(),name='detail'),
    path('users/',UserList.as_view(),name='users'),
    path('users/<int:pk>',UserDetailView.as_view(),name='users_detail'),
    path('<slug:slug>',ArticleDetailView_slug.as_view(),name='detail_slug'),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
]
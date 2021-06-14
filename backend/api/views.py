from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

from blog.models import Articles
from .serializers import ArticleSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

class ArticleListView(ListAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
    
class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
    
class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsAdminUser,)
    
class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsAdminUser,)
    
class ArticleDetailView_slug(RetrieveUpdateDestroyAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
    lookup_field='slug'
from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView
# Create your views here.

from blog.models import Articles
from .serializers import ArticleSerializer

class ArticleListView(ListAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
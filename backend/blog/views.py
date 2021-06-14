from django.shortcuts import render
from django.views.generic import ListView
from .models import Articles

# Create your views here.
class ArticleView(ListView):
    def get_queryset(self):
        return Articles.objects.filter(status=True)
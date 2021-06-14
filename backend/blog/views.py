from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Articles

# Create your views here.
class ArticleView(ListView):
    def get_queryset(self):
        return Articles.objects.filter(status=True)
    
class ArticleDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(Articles.objects.filter(status=True),pk=self.kwargs.get('pk'))
    
class ArticleDetailView_slug(DetailView):
    def get_object(self):
        return get_object_or_404(Articles.objects.filter(status=True),slug=self.kwargs.get('slug'))
    
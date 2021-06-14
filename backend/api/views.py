from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

from blog.models import Articles
from .serializers import ArticleSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser,IsAuthorOrReadOnly,IsStaffOrReadOnly,IsSuperuserOrStaffReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleListView(ListCreateAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
    
class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=(IsStaffOrReadOnly,IsAuthorOrReadOnly)
    
class UserList(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperuserOrStaffReadOnly,)
    
class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperuserOrStaffReadOnly,)
    
class ArticleDetailView_slug(RetrieveUpdateDestroyAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
    lookup_field='slug'
    
class RevorkeToken(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self, request):
        request.auth.delete()
        return Response({"method":"you are loged out"},status=204)
    
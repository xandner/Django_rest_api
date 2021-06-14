from django.db.models import fields
from rest_framework import serializers
from blog.models import Articles
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articles
        
        """ we need this """
        # fields=(
        #     'title',
        #     'slug',
        #     'author',
        #     'content',
        #     'published',
        #     'status'
        # )
        
        """ we dont need this """
        exclude=('created','updated')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
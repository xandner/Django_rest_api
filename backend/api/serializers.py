from django.db.models import fields
from rest_framework import serializers
from blog.models import Articles

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
        
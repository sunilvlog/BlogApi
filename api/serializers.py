from rest_framework import serializers
from api.models import ArticleName
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArticleName
        fields = ('id','title','descryption')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","password")
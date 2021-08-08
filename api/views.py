from django.shortcuts import render,HttpResponse
from api.models import ArticleName
from django.contrib.auth.models import User
from api.serializers import ArticleSerializer,UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.
def Article(request):
    return HttpResponse("Hello Django Which is popular language based on python")

class ArticleViewset(viewsets.ModelViewSet):
    queryset = ArticleName.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
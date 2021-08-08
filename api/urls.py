from django.urls import path,include
from api.views import Article, ArticleViewset, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('article',ArticleViewset,basename='article')
router.register('user',UserViewSet)

urlpatterns = [
    path("data/",Article),
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api_token/', obtain_auth_token)
    
]
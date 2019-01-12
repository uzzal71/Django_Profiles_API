from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-api/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]
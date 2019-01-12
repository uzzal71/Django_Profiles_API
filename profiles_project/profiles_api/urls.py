from django.urls import path
from .import views

urlpatterns = [
    path('hello-api/', views.HelloAPIView.as_view())
]
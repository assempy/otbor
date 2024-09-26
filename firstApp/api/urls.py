from django.urls import path
from .views import firstFuntion

urlpatterns = [
    path('first/', firstFuntion),
]

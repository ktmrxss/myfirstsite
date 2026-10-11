from django.urls import path
from .views import friends

urlpatterns = [
    path( '', friends, name='friends'),
]
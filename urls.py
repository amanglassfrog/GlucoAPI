from django.urls import path
from .view import recommendations

urlpatterns = [
    path('recommendations/', recommendations, name='recommendations'),
]
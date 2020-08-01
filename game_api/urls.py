from django.urls import path
from .views import game_list

urlpatterns = [
    path('game/', game_list)
]

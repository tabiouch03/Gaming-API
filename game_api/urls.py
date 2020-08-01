from django.urls import path
from .views import game_list, game_detail

urlpatterns = [
    path('game/', game_list),
    path('detail/<int:pk>', game_detail)
]

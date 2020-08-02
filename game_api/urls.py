from django.urls import path
from .views import game_list, game_detail, news_list, news_detail

urlpatterns = [
    path('game/', game_list),
    path('detail/<int:pk>', game_detail),
    path('news/', news_list),
    path('news-detail/<int:pk>', news_detail)
]

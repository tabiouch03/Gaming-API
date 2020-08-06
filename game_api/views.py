from .models import Game, Genre, News
from .serializers import GameSerializer, NewsSerializer, GenreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def gameAPI(request):
  api_urls = {
    'Games List' : '/game/',
    'Game Details' : '/detail/<int:pk>',
    'News List' : '/news/',
    'News Detail' : '/news-detail/<int:pk>'
  }

  return Response(api_urls)

##########################
## ALL METHOD FOR GAMES ##
##########################

@api_view(['GET', 'POST'])
def game_list(request):

  if request.method == 'GET':
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = GameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
  try:
    game = Game.objects.get(pk=pk)

  except Game.DoesNotExist:
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = GameSerializer(game)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = GameSerializer(game, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    game.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

##########################
## ALL METHOD FOR NEWS  ##
##########################

@api_view(['GET', 'POST'])
def news_list(request):

  if request.method == 'GET':
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def news_detail(request, pk):
  try:
    news = News.objects.get(pk=pk)

  except News.DoesNotExist:
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = NewsSerializer(news)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = NewsSerializer(news, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    news.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def genre_list(request):

  if request.method == 'GET':
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer =GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk):
  try:
    genre = Genre.objects.get(pk=pk)

  except Genre.DoesNotExist:
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = GenreSerializer(game)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = GenreSerializer(genre, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    genre.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
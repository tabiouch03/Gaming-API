from .models import Game, Genre
from .serializers import GameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

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
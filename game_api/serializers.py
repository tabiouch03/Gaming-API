from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
    class Meta:
      model = Game
      fields = '__all__'
      depth = 1


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
      model = Genre

class PlateformSeriliazer(serializers.ModelSerializer):
    class Meta:
      model = Plateform

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
      model = News
      fields = '__all__'
      

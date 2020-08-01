from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Game Model
class Game(models.Model):
  title = models.CharField(max_length=50)
  editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
  cover = models.CharField(max_length=500)
  resume = models.TextField()
  note = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
  available = models.BooleanField(default=True)
  trailer = models.CharField(max_length=500)
  date = models.DateTimeField(auto_now_add=True)
  genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

  def __str__(self):
    return self.title

# Editeur Model
class Editor(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

# Genre Model
class Genre(models.Model):
  genre = models.CharField(max_length=15)

  def __str__(self):
    return self.genre
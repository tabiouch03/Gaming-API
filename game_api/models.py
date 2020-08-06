from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms 


# Game Model
class Game(models.Model):
  title = models.CharField(max_length=50)
  editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
  cover = models.CharField(max_length=500)
  resume = models.TextField()
  average = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
  available = models.BooleanField(default=True)
  trailer = models.CharField(max_length=500, null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)
  genre = models.ManyToManyField('Genre', blank=True)
  plateform = models.ManyToManyField('Plateform', blank=True)
  test_img = models.CharField(max_length=255, null=True, blank=True)
  test_img1 = models.CharField(max_length=255, null=True, blank=True)
  test_img2 = models.CharField(max_length=255, null=True, blank=True)
  test_img3 = models.CharField(max_length=255, null=True, blank=True)
  test_img4 = models.CharField(max_length=255, null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  description1 = models.TextField(null=True, blank=True)
  description2 = models.TextField(null=True, blank=True)
  description3 = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.title

# News Model
class News(models.Model):
  title = models.CharField(max_length=100)
  resume = models.TextField()
  image = models.CharField(max_length=255)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title


# Editeur Model
class Editor(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

# Genre Model
class Genre(models.Model):
  name = models.CharField(max_length=15)

  def __str__(self):
    return self.name

# Platefrom Model
class Plateform(models.Model):
  console = models.CharField(max_length=15)

  def __str__(self):
    return self.console
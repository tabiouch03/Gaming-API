from django.contrib import admin
# Import du modele dans l'interface d'administration
from .models import *

class GameAdmin(admin.ModelAdmin):
  list_filter = ['genre']
  search_fields = ['title']
  ordering = ['id']

admin.site.register(Game,GameAdmin)
admin.site.register(Plateform)
admin.site.register(Genre)
admin.site.register(Editor)
admin.site.register(News)



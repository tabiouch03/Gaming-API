from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='api')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game_api.urls'))
]


from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include("display.urls")),
    path('magic',include("magic.urls"))
]

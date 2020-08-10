from django.urls import path
from . import views


app_name = 'recipe_site'
urlpatterns = [
    path('', views.request, name='request'),
]
from django.urls import path
from . import views

app_name = 'scrap_soup'

urlpatterns = [
    path("start/", views.start_scraping, name="start"),
   
]
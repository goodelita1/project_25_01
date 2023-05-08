from django.urls import path
from . import views

app_name = 'gits'

urlpatterns = [
    path("hashinfo/", views.hash_info, name="hashinfo"),
    path("implantinfo/", views.implant_info, name="implantinfo"),
    path('sendmail/', views.email_handler, name='sendmail')
]
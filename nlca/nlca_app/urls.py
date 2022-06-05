from django.urls import path
from . import views

# URL Configs
urlpatterns = [path("", views.home, name="name_home"),
                path("encr", views.encr, name="name_encr"),
              ]
from django.urls import path
from . import views

# URL Configs
urlpatterns = [path("encryption_home", views.home, name="name_home"),
                path("encr", views.encr, name="name_encr"),
                path("decr", views.decr, name="name_decr"),
                path("decr_home", views.decr_home, name="name_decr_home"),
                path("", views.encryption_home, name="name_encryption"),
                path("decryption_home", views.decryption_home, name="name_decryption"),
              ]
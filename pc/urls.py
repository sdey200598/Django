from django.contrib import admin
from django .urls import path
from pc import views

urlpatterns=[
    path("",views.index,name="pc"),
    path("about",views.about,name="about"),
    path("contacts",views.contacts,name="contacts")
]
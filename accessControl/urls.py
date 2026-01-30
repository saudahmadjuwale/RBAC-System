from django.contrib import admin
from . import views
from django.urls import path
app_name = "accessControl"
urlpatterns = [
    path('create_permission/', views.create_permission,name="create_permission"),
    path('create_role/', views.create_role,name="create_role"),
]

from django.urls import path

from . import views

app_name = "Clase"

urlpatterns = [
    path('', views.home, name="home"),
    path('comision_create/', views.create, name="comision_create"),
    path('estudiante_create/', views.estudiante_create, name="estudiante_create"),
    path('estudiante_home/', views.estudiante_home, name="estudiante_home"),
]
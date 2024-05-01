from django.urls import path

from . import views

app_name = "Clase"

urlpatterns = [
    path('', views.home, name="home"),
    path('comision_create/', views.create, name="comision_create"),
    path('estudiante_create/', views.estudiante_create, name="estudiante_create"),
    path('estudiante_home/', views.estudiante_home, name="estudiante_home"),
    path('profesor_home/', views.profesor_home, name="profesor_home"),
    path('profesor_create/', views.profesor_create, name="profesor_create"),
    path('curso_home/', views.curso_home, name="curso_home"),
    path('curso_create/', views.curso_create, name="curso_create"),
]
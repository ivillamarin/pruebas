from django.urls import path
from django.contrib.auth.views import LogoutView
from App.views import *

urlpatterns = [
    path('inicio', inicio),
    path('cursos',curso, name="cursos"),
    path('estudiantes', estudiantes, name="estudiantes"),
    path('profesores', profesores, name="profesores" ),
    path('setEstudiante/', setEstudiante, name="setEstudiante"),
    path('getProfesores/', getProfesores, name="getProfesores"),
    path('buscarProfesor/', buscarProfesor, name="buscarProfesor"),
    path('login/', loginWeb, name="login"),
    path('eliminarEstudiante/<nombre_estudiante>', eliminarEstudiante, name="eliminarEstudiante"),
    path('editarEstudiante/<nombre_estudiante>', editarEstudiante, name="editarEstudiante"),
    path('registro/', registro, name="registro"),
    path('Logout', LogoutView.as_view(template_name = 'App/login.html'), name="Logout"),
]

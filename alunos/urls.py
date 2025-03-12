from django.urls import path
from . import views

urlpatterns = [
    path('criar_aluno/', views.criar_aluno, name="criar_aluno")
]
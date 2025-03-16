from django.urls import path
from . import views

#url para pagina de criação do cadastro do aluno
urlpatterns = [
    path('criar_aluno/', views.criar_aluno, name="criar_aluno")
]
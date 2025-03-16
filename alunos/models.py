from django.db import models

# Create your models here.
#model aluno, cria uma tabela no banco de dados
class Aluno(models.Model):
    #valores da tabela
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    #stringifica o nome
    def __str__(self):
        return self.nome

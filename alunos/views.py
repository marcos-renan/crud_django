from django.shortcuts import render

# Create your views here.
def criar_aluno(request):
    return render(request, 'criar_aluno.html')
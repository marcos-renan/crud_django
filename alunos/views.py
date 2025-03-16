from django.shortcuts import render, redirect
from .models import Aluno

# Create your views here.
def criar_aluno(request):
    #caso o metodo seja get
    if request.method == 'GET':
        #retorne a pagina inicial
        return render(request, 'criar_aluno.html')
    #caso seja posr
    elif request.method =='POST':
        #capture os dados inseridos nos campos
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        #armazene eles nas variaveis da model
        aluno = Aluno(
            nome = nome,
            email = email,
        )
        #salve no banco de dados
        aluno.save()
        #redirecione para a pagina inicial
        return redirect('criar_aluno')
        
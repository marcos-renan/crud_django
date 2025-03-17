from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno

# Create your views here.
def criar_aluno(request):
    #caso o metodo seja get
    if request.method == 'GET':
        #obtenha todos os dados do banco de dados
        alunos = Aluno.objects.all()
        #retorne a pagina inicial
        return render(request, 'criar_aluno.html', {'alunos':alunos})
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
        
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('criar_aluno')

def editar_aluno(request, id):
    #obtem os dados do banco
    aluno = get_object_or_404(Aluno, id=id)
    #pega os valores dos campos
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    #atribui novos valores
    aluno.nome = nome
    aluno.email = email
    #salva no banco
    aluno.save()
    #redireciona para a pagina inicial
    return redirect('criar_aluno')
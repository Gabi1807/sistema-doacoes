from django.shortcuts import render, redirect
from .models import Doador, Beneficiario, Item, Doacao
from .forms import DoadorForm, BeneficiarioForm, ItemForm, DoacaoForm


# Página inicial (HOME)
def home(request):
    doadores = Doador.objects.all()
    beneficiarios = Beneficiario.objects.all()
    doacoes = Doacao.objects.all()

    return render(
        request,
        'gestao/home.html',
        {
            'doadores': doadores,
            'beneficiarios': beneficiarios,
            'doacoes': doacoes,
        }
    )


# Cadastrar DOADOR
def cadastrar_doador(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = DoadorForm()

    return render(
        request,
        'gestao/cadastrar_doador.html',
        {'form': form}
    )


# Cadastrar BENEFICIÁRIO
def cadastrar_beneficiario(request):
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = BeneficiarioForm()

    return render(
        request,
        'gestao/cadastrar_beneficiario.html',
        {'form': form}
    )


# Cadastrar ITEM
def cadastrar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ItemForm()

    return render(
        request,
        'gestao/cadastrar_item.html',
        {'form': form}
    )


# Registrar DOAÇÃO
def cadastrar_doacao(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = DoacaoForm()

    return render(
        request,
        'gestao/cadastrar_doacao.html',
        {'form': form}
    )

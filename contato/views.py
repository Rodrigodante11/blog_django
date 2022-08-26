from django.shortcuts import render

from contato.contato_form import formContato


def contato(request):
    return render(request, 'contato/contato.html',  {'form': formContato()})


def processa_contato(request):
    return render(request, 'contato/contato.html', {'form': formContato()})

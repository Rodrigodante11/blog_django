from django.shortcuts import render
from django.contrib import messages
from contato.contato_form import formContato


def contato(request):
    return render(request, 'contato/contato.html',  {'form': formContato()})


def processa_contato(request):
    if request.method == 'POST':
        contato = formContato(request.POST)
        if contato.is_valid():
            assunto = contato.cleaned_data['assunto']
            messages.success(request, 'Mensagem encaminha com sucess')
            messages.error(request, 'Mensagem Nao Enviada')
            return render(request, 'contato/contato.html', {'form': formContato()})
        else:
            messages.error(request, 'Mensagem Nao Enviada')
            return render(request, 'contato/contato.html', {'form': contato})
    return render(request, 'contato/contato.html', {'form': formContato()})

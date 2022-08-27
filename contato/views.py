from django.shortcuts import render
from django.contrib import messages
from contato.contato_form import formContato
from django.core.mail import send_mail
from core import settings


def contato(request):
    return render(request, 'contato/contato.html', {'form': formContato()})


def processa_contato(request):
    if request.method == 'POST':
        contato = formContato(request.POST)
        if contato.is_valid():

            messages.success(request, 'Mensagem encaminha com sucess')
            enviar_email(contato)
            # messages.error(request, 'Mensagem Nao Enviada')
            return render(request, 'contato/contato.html', {'form': formContato()})
        else:
            messages.error(request, 'Mensagem Nao Enviada')
            return render(request, 'contato/contato.html', {'form': contato})
    return render(request, 'contato/contato.html', {'form': formContato()})


def enviar_email(contato):
    send_mail(
        contato.cleaned_data['assunto'],
        contato.cleaned_data['mensagem'],
        settings.EMAIL_HOST_USER,
        [contato.cleaned_data['email']],
        fail_silently=False,
    )

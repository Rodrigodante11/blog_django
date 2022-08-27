from django.shortcuts import render
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from contato.contato_form import formContato
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from core import settings
from django.http import HttpResponse


def contato(request):
    return render(request, 'contato/contato.html', {'form': formContato()})


def processa_contato(request):
    if request.method == 'POST':
        contato = formContato(request.POST)
        if contato.is_valid():

            try:

                enviar_email_com_template(contato)
                messages.success(request, 'Mensagem encaminha com sucess')
                # messages.error(request, 'Mensagem Nao Enviada')
                return render(request, 'contato/contato.html', {'form': formContato()})
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

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


def enviar_email_com_template(contato):
    html_content = render_to_string(
        'email_template/confirmacao_mensagem.html',
        {'nome': contato.cleaned_data['nome'],
         'assunto': contato.cleaned_data['assunto']}
    )
    text_content = strip_tags(html_content)  # igual a de cima so nao tem as tags HTML

    msg = EmailMultiAlternatives(contato.cleaned_data['assunto'], text_content, settings.EMAIL_HOST_USER,
                                 [contato.cleaned_data['email']])

    msg.attach_alternative(html_content, "text/html")
    msg.send()



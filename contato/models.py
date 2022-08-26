from django.db import models

CHOICES_ASSUNTO = [
    ('', 'Selecione um assunto'),
    ('descontos', 'Descontos'),
    ('consultoria', 'Consultoria'),
    ('freelance', 'Freelance'),
    ('elogios', 'Elogios'),
    ('reclamações', 'Reclamações'),
    ('outros', 'Outros'),
]


class Contato(models.Model):
    assunto = models.CharField(choices=CHOICES_ASSUNTO, max_length=100, default="")
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mensagem = models.CharField(max_length=100)

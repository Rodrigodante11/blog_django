# Generated by Django 3.2.15 on 2022-08-14 02:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_conteudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

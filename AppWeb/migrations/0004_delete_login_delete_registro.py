# Generated by Django 4.2.3 on 2023-08-22 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0003_comprador_vendedor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-22 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0004_delete_login_delete_registro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedor',
            name='profesion',
        ),
    ]

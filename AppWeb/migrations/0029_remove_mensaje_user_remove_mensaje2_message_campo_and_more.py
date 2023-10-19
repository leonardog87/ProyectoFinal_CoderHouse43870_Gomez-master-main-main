# Generated by Django 4.2.3 on 2023-09-05 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppWeb', '0028_remove_mensaje_message_campo_remove_mensaje2_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mensaje2',
            name='message_campo',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='mensaje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='AppWeb.blog'),
        ),
        migrations.AddField(
            model_name='mensaje2',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje2',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 4.2.3 on 2023-09-05 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppWeb', '0019_alter_mensaje_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
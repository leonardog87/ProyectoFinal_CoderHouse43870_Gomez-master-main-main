# Generated by Django 4.2.3 on 2023-09-07 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0043_alter_blog_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blogimg'),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-11 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='Autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

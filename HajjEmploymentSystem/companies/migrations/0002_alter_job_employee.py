# Generated by Django 4.1 on 2022-08-03 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1 on 2022-08-03 19:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0002_alter_job_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='applicants',
            field=models.ManyToManyField(null=True, related_name='applicants', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1 on 2022-08-03 21:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_job_applicants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applicants',
            field=models.ManyToManyField(related_name='applicants', to=settings.AUTH_USER_MODEL),
        ),
    ]

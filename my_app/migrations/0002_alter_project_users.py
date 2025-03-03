# Generated by Django 5.0.7 on 2024-11-25 13:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='projects_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]

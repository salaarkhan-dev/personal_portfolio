# Generated by Django 3.1 on 2020-08-07 04:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]

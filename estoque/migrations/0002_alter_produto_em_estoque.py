# Generated by Django 5.0.1 on 2024-01-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='em_estoque',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.2 on 2024-04-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='training_type',
            field=models.CharField(blank=True, choices=[('Normal Training', 'Normal Training'), ('Personal Training', 'Personal Training')], max_length=50, null=True),
        ),
    ]

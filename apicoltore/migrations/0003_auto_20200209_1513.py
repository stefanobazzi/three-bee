# Generated by Django 3.0.3 on 2020-02-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiario', '0004_auto_20200209_1513'),
        ('apicoltore', '0002_apicoltore_apiari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apicoltore',
            name='apiari',
            field=models.ManyToManyField(related_name='apicoltori', to='apiario.Apiario'),
        ),
    ]

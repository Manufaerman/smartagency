# Generated by Django 3.2.9 on 2021-11-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitehouse', '0005_categorias'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorias',
            old_name='Updated',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='vivienda',
            name='categoria',
            field=models.ManyToManyField(to='whitehouse.Categorias'),
        ),
    ]

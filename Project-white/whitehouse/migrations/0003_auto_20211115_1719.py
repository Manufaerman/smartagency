# Generated by Django 3.2.9 on 2021-11-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitehouse', '0002_auto_20211115_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivienda',
            name='foto1',
            field=models.ImageField(upload_to='whitehouse/static/img/'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='foto2',
            field=models.ImageField(upload_to='whitehouse/static/img/'),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='foto3',
            field=models.ImageField(upload_to='whitehouse/static/img/'),
        ),
    ]

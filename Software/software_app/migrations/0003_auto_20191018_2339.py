# Generated by Django 2.2.6 on 2019-10-19 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_app', '0002_auto_20191018_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='fecha',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fechaDeNacimiento',
            field=models.CharField(max_length=30),
        ),
    ]

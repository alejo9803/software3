# Generated by Django 2.2.6 on 2019-10-19 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('software_app', '0006_auto_20191019_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='idRespuesta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='software_app.Respuesta'),
        ),
    ]

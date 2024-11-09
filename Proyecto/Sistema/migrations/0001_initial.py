# Generated by Django 5.0.6 on 2024-06-14 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.TextField(max_length=25)),
                ('Precio', models.FloatField()),
                ('Descripcion', models.TextField(max_length=50)),
            ],
        ),
    ]
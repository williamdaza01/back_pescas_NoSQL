# Generated by Django 4.1.3 on 2022-11-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenca',
            fields=[
                ('ID_CUENCA', models.IntegerField(db_column='ID_CUENCA', primary_key=True, serialize=False)),
                ('NOMBRE_CUENCA', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'Cuenca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metodo',
            fields=[
                ('ID_METODO', models.IntegerField(db_column='ID_METODO', primary_key=True, serialize=False)),
                ('NOMBRE_METODO', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'Metodo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pesca',
            fields=[
                ('ID_PESCA', models.IntegerField(primary_key=True, serialize=False)),
                ('FECHA_PESCA', models.TextField(db_column='FECHA_PESCA')),
                ('PESO_PESCADO', models.TextField(db_column='PESO_PESCADO')),
            ],
            options={
                'db_table': 'Pesca',
                'managed': False,
            },
        ),
    ]
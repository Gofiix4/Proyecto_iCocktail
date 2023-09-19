# Generated by Django 3.2.4 on 2023-09-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idAlumno', models.IntegerField(db_column='idAlumno', primary_key=True, serialize=False)),
                ('nameAlumno', models.CharField(db_column='nameAlumno', max_length=100)),
            ],
            options={
                'db_table': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('tipoGenero', models.TextField(db_column='tipoGenero')),
            ],
            options={
                'db_table': 'Generos',
            },
        ),
    ]

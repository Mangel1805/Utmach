# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contrasena', models.CharField(max_length=50, verbose_name='Contrasena:')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstadoMatricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=10, verbose_name='Estado:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstadoPersona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=8, verbose_name='Estado:')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contrasena', models.CharField(max_length=50, verbose_name='Contrasena:')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicio', models.TimeField(verbose_name='Hora Inicio:')),
                ('fin', models.TimeField(verbose_name='Hora Fin:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre:')),
                ('profesor', models.ForeignKey(verbose_name='Docente:', blank=True, to='sistema.Docente', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ano', models.DateField(verbose_name='A\xf1o:')),
                ('estado', models.ForeignKey(verbose_name='Estado:', blank=True, to='sistema.EstadoMatricula', null=True)),
                ('estudiante', models.ForeignKey(verbose_name='Estudiante:', blank=True, to='sistema.Estudiante', null=True)),
                ('horario', models.ForeignKey(verbose_name='Horario:', blank=True, to='sistema.Hora', null=True)),
                ('materia', models.ForeignKey(verbose_name='Materia:', blank=True, to='sistema.Materia', null=True)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descipcion', models.CharField(max_length=40, verbose_name='Nivel:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deberes', models.FloatField(verbose_name='Deberes:')),
                ('participacionClases', models.FloatField(verbose_name='Participacion:')),
                ('oral', models.FloatField(verbose_name='Leccion oral:')),
                ('escrita', models.FloatField(verbose_name='Leccion Escrita:')),
                ('examen', models.FloatField(verbose_name='Examen:')),
                ('total', models.FloatField(verbose_name='Total:')),
                ('matricula', models.ForeignKey(verbose_name='Matricuala:', blank=True, to='sistema.Matricula', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paralelo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descipcion', models.CharField(max_length=40, verbose_name='Paralelo:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.CharField(max_length=10, verbose_name='Periodo:')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=10, verbose_name='Cedula:')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre:')),
                ('apellido', models.CharField(max_length=80, verbose_name='Apellido:')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono:', blank=True)),
                ('celular', models.CharField(max_length=10, verbose_name='Celular:', blank=True)),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion:')),
                ('email', models.EmailField(max_length=75, verbose_name='Email:')),
                ('estado', models.ForeignKey(verbose_name='Estado:', blank=True, to='sistema.EstadoPersona', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descipcion', models.CharField(max_length=20, verbose_name='Descripcion:')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo',
            field=models.ForeignKey(verbose_name='Tipo:', blank=True, to='sistema.TipoPersona', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matricula',
            name='nivel',
            field=models.ForeignKey(verbose_name='Nivel:', blank=True, to='sistema.Nivel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matricula',
            name='paralelo',
            field=models.ForeignKey(verbose_name='Paralelo:', blank=True, to='sistema.Paralelo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matricula',
            name='periodo',
            field=models.ForeignKey(verbose_name='Periodo:', blank=True, to='sistema.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='persona',
            field=models.ForeignKey(verbose_name='Persona:', blank=True, to='sistema.Persona', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='docente',
            name='persona',
            field=models.ForeignKey(verbose_name='Persona:', blank=True, to='sistema.Persona', null=True),
            preserve_default=True,
        ),
    ]

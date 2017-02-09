# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigInscrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('codigo', models.CharField(max_length=5)),
                ('cantidad', models.IntegerField()),
                ('cant_rondas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConfigTorneo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
                ('config_inscrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.ConfigInscrito')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('iniciales', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilJuego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(choices=[('ALE', 'Aleatorio'), ('ORC', 'Orco'), ('HUM', 'Humano'), ('ELF', 'Elfo nocturno')], default='ALE', max_length=20)),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.Juego')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Ronda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('config_inscrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.ConfigInscrito')),
            ],
        ),
        migrations.CreateModel(
            name='Toreno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Versus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapa', models.CharField(blank=True, max_length=50, null=True)),
                ('replay', models.CharField(blank=True, max_length=50, null=True)),
                ('nro_versus', models.IntegerField(blank=True, null=True)),
                ('inscrito1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugador1', to='torneo.Inscripcion')),
                ('inscrito2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugador2', to='torneo.Inscripcion')),
                ('inscrito_ganador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ganador', to='torneo.Inscripcion')),
                ('ronda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='torneo.Ronda')),
                ('versus_ganador1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ganador_anterior1', to='torneo.Versus')),
                ('versus_ganador2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ganador_anterior2', to='torneo.Versus')),
            ],
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='torneo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.Toreno'),
        ),
        migrations.AddField(
            model_name='configtorneo',
            name='juego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.Juego'),
        ),
        migrations.AddField(
            model_name='configtorneo',
            name='torneo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.Toreno'),
        ),
    ]

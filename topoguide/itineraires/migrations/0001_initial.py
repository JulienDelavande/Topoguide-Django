# Generated by Django 4.0.4 on 2022-04-19 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itineraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom de la sortie', models.CharField(max_length=200)),
                ('Point de départ', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=1000)),
                ('altitude_de_depart', models.FloatField()),
                ('altitude_min', models.FloatField()),
                ('altitude_max', models.FloatField()),
                ('denivele_positif_cumule', models.FloatField()),
                ('denivele_negatif_cumule', models.FloatField()),
                ('Durée estimée (en h)', models.IntegerField()),
                ('difficulte_estimee', models.IntegerField(choices=[(1, 'Très facile'), (2, 'Facile'), (3, 'Moyenne'), (4, 'Difficile'), (5, 'Très difficile')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Sortie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sortie', models.DateField()),
                ('Durée réelle (en h)', models.IntegerField()),
                ('difficulte_estimee', models.IntegerField(choices=[(1, 'Très facile'), (2, 'Facile'), (3, 'Moyenne'), (4, 'Difficile'), (5, 'Très difficile')], default=3)),
                ('itineraire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraires.itineraire')),
            ],
        ),
    ]
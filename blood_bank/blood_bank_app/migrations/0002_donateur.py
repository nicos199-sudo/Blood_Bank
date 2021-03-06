# Generated by Django 2.0.13 on 2020-06-23 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('Tel', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=10)),
                ('nationalite', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=30)),
                ('adresse', models.CharField(max_length=30)),
                ('groupe_sanguin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blood_bank_app.Sang')),
            ],
        ),
    ]

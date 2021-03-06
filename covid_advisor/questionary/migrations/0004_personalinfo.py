# Generated by Django 3.0.4 on 2020-03-15 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0003_auto_20200315_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(blank=True, max_length=120)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('questionary', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='questionary.Questionary')),
            ],
        ),
    ]

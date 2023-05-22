# Generated by Django 4.2.1 on 2023-05-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rand', models.FloatField()),
                ('dollar', models.FloatField()),
                ('australian_dollar', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('story', models.TextField()),
            ],
        ),
    ]

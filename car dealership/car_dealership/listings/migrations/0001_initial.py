# Generated by Django 4.0.5 on 2022-06-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('milage', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]

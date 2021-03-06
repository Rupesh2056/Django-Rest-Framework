# Generated by Django 3.1a1 on 2021-05-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Artist', models.CharField(max_length=50)),
                ('Tracks', models.IntegerField()),
                ('Length', models.FloatField()),
                ('Rating', models.FloatField(null=True)),
            ],
        ),
    ]

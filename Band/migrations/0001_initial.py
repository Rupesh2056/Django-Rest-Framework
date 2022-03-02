# Generated by Django 3.1a1 on 2021-05-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Genre', models.CharField(max_length=50)),
                ('Established', models.DateTimeField(null=True)),
                ('Albums', models.IntegerField()),
            ],
        ),
    ]
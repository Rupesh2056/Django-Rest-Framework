# Generated by Django 3.1a1 on 2021-05-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Band', '0002_auto_20210502_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='Established',
            field=models.DateField(blank=True, null=True),
        ),
    ]
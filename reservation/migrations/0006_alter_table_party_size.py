# Generated by Django 4.0.1 on 2022-01-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_alter_table_party_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='party_size',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('4', '3'), ('6', '4'), ('8', '8')], max_length=1),
        ),
    ]

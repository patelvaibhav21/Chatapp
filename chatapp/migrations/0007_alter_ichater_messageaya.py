# Generated by Django 4.1.1 on 2022-12-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_alter_ichater_messageaya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ichater',
            name='messageaya',
            field=models.CharField(default='nothing', max_length=100000000000000000),
        ),
    ]

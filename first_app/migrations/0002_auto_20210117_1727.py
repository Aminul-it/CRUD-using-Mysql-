# Generated by Django 3.0.6 on 2021-01-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='relase_date',
            field=models.DateField(choices=[(1, 'worst'), (2, 'bad'), (3, 'not bad'), (4, 'good'), (5, 'Excellent')]),
        ),
    ]

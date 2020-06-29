# Generated by Django 2.2.6 on 2020-04-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_eventsdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsdata',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
        migrations.AlterField(
            model_name='eventsdata',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
    ]

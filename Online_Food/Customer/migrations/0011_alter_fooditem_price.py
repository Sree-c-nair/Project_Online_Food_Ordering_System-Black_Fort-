# Generated by Django 4.1.7 on 2023-03-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0010_fooditem_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-22 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_alter_customers_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='food',
            new_name='fooditem',
        ),
    ]

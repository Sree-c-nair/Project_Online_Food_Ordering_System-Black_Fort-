# Generated by Django 4.1.7 on 2023-03-24 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0011_alter_fooditem_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='user',
            new_name='user1',
        ),
    ]
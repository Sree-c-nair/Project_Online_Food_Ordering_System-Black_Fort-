# Generated by Django 4.1.7 on 2023-03-24 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0012_rename_user_customers_user1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='user1',
            new_name='user',
        ),
    ]
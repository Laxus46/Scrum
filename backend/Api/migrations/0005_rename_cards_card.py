# Generated by Django 4.2.1 on 2023-06-13 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_cards'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cards',
            new_name='Card',
        ),
    ]

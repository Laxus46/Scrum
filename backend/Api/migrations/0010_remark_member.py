# Generated by Django 4.2.1 on 2023-06-13 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_remove_card_member_remove_card_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='remark',
            name='member',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Api.teammember'),
        ),
    ]

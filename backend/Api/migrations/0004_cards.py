# Generated by Django 4.2.1 on 2023-06-13 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_rename_role_teammember_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.member')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.position')),
                ('sprint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.sprint')),
            ],
        ),
    ]

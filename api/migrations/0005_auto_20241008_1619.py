# Generated by Django 3.2.25 on 2024-10-08 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_laptop_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lendoutpc',
            old_name='description',
            new_name='pc_description',
        ),
        migrations.RenameField(
            model_name='lendoutpc',
            old_name='laptop_name',
            new_name='pc_name',
        ),
        migrations.RenameField(
            model_name='lendoutpc',
            old_name='owner',
            new_name='pc_owner',
        ),
        migrations.RenameField(
            model_name='lendoutpc',
            old_name='status',
            new_name='pc_status',
        ),
    ]

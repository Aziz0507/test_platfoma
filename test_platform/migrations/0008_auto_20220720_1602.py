# Generated by Django 3.2.7 on 2022-07-20 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_platform', '0007_verifity_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verifity_models',
            old_name='option_user',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='verifity_models',
            old_name='questions_id',
            new_name='quiz_id',
        ),
        migrations.RenameField(
            model_name='verifity_models',
            old_name='thems',
            new_name='them',
        ),
        migrations.RenameField(
            model_name='verifity_models',
            old_name='users',
            new_name='user',
        ),
    ]
# Generated by Django 3.2.7 on 2022-07-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_platform', '0005_alter_test_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_question',
            name='answer',
            field=models.IntegerField(help_text='Напишите правильный вариант'),
        ),
    ]
# Generated by Django 3.2.7 on 2022-07-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='Тип Теста')),
            ],
            options={
                'verbose_name': 'Тип теста',
                'verbose_name_plural': 'Типы тестов',
            },
        ),
    ]

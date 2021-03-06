# Generated by Django 3.2.7 on 2022-07-04 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_platform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catigoriy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catigoriy', models.CharField(max_length=35, verbose_name='Тип категории')),
            ],
            options={
                'verbose_name': 'Тип категории',
                'verbose_name_plural': 'Типы категории',
            },
        ),
        migrations.CreateModel(
            name='Test_Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=50, verbose_name='Тип тестов')),
                ('types_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_platform.catigoriy', verbose_name='категория теста')),
            ],
            options={
                'verbose_name': 'Тип теста',
                'verbose_name_plural': 'Типы тестов',
            },
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]

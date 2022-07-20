# Generated by Django 3.2.7 on 2022-07-19 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_platform', '0006_alter_test_question_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verifity_Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_user', models.IntegerField(verbose_name='Выбор пользователя')),
                ('questions_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_platform.test_question', verbose_name='ID вопроса')),
                ('thems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_platform.test_types', verbose_name='Тема теста')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Выбор пользователя',
                'verbose_name_plural': 'Выборы пользователей',
            },
        ),
    ]

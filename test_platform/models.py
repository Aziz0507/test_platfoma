from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catigoriy(models.Model):
    catigoriy = models.CharField(max_length=35, verbose_name='Тип категории')

    class Meta:
        verbose_name = 'Тип категории'
        verbose_name_plural = 'Типы категории'
    
    def __str__(self):
        return self.catigoriy

class Test_Types(models.Model):
    types_catigoriy = models.ForeignKey(Catigoriy, on_delete = models.CASCADE, verbose_name = 'категория теста')
    types     = models.CharField(max_length=50, verbose_name = 'Тип тестов') 

    class Meta:
        verbose_name = 'Тип теста'
        verbose_name_plural = 'Типы тестов'
    
    def __str__(self):
        return self.types

class Test_question(models.Model):
    test_type = models.ForeignKey(Test_Types, on_delete = models.CASCADE, verbose_name = 'Тип тестов')
    question  = models.TextField(verbose_name='Опишите Вопрос')
    options_A = models.CharField(max_length = 50, verbose_name = 'Вориант А')
    options_B = models.CharField(max_length = 50, verbose_name = 'Вориант B')
    options_C = models.CharField(max_length = 50, verbose_name = 'Вориант C')
    options_D = models.CharField(max_length = 50, verbose_name = 'Вориант D')
    answer    = models.IntegerField(help_text= 'Напишите правильный вариант')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
    
    def __str__(self):
        return f"Категория : {self.test_type}, вопрос : {self.id}"


class Verifity_Models(models.Model):
    users        = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name = 'пользователь' )
    thems        = models.ForeignKey(Test_Types, on_delete = models.CASCADE, verbose_name = 'Тема теста')
    questions_id = models.ForeignKey(Test_question, on_delete = models.CASCADE, verbose_name = 'ID вопроса')
    option_user  = models.IntegerField(verbose_name = 'Выбор пользователя')

    class Meta:
        verbose_name = 'Выбор пользователя'
        verbose_name_plural = 'Выборы пользователей'

    def __str__(self):
        return f"Пользователь {self.users}, Вопрос {self.thems}"
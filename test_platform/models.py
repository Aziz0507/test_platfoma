from django.db import models

# Create your models here.
class Catigoriy(models.Model):
    catigoriy = models.CharField(max_length=35, verbose_name='Тип категории')

    class Meta:
        verbose_name = 'Тип категории'
        verbose_name_plural = 'Типы категории'
    
    def __str__(self):
        return self.catigoriy

class Test_Types(models.Model):
    types_cat = models.ForeignKey(Catigoriy, on_delete = models.CASCADE, verbose_name = 'категория теста')
    types     = models.CharField(max_length=50, verbose_name = 'Тип тестов') 

    class Meta:
        verbose_name = 'Тип теста'
        verbose_name_plural = 'Типы тестов'
    
    def __str__(self):
        return self.types


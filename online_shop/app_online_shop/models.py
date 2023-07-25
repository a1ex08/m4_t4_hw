from django.db import models

# Create your models here.

# Создаём класс с описанием структуры таблицы (наследование от model)
class OnlineShop(models.Model):
    # создаём заголовок
    title = models.CharField('Заголовок', max_length=128)
    # Описание
    # TextField - строковое поле большого размера
    description = models.TextField('Описание')
    # decimal как float
    # decimal_places колво знаков после запятой
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    auction = models.BooleanField('Торг', help_text='Укажите, уместен ли торг')

    # auto_now_add автополучение даты при создании auto_now при добавлении
    created_time = models.DateTimeField(auto_now_add=True)

    update_time = models.DateTimeField(auto_now=True)

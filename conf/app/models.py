import random
import string
from django.contrib.auth.models import AbstractUser
from django.db import models


def random_number():
    """Создание сгенерированного id пользователя из 3 букв и 2 чисел"""
    random_id_user = str(
        ''.join(random.choices(string.ascii_lowercase, k=3)) + ''.join(random.choices(string.digits, k=2)))
    return random_id_user


class CustomUser(models.Model):
    """Пользователи"""
    name = models.CharField(verbose_name="Имя пользователя", max_length=20)
    avatar = models.FileField(verbose_name='Аватар', default='ava.png')
    random_id = models.CharField(verbose_name='Сгенерированный id', max_length=5, unique=True, default=random_number,
                                 blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = "name",

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Проверяем на уникальность Сгенерированный id для пользователя в момент его регистрации
        if self.id is None:
            while CustomUser.objects.filter(random_id=self.random_id):
                self.random_id = random_number()
        super().save(*args, **kwargs)

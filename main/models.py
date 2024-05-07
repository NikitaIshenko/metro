from django.db import models

class Dogovor(models.Model):
    last_name = models.CharField('Фамилия', max_length=155)
    first_name = models.CharField('Имя', max_length=155)
    patronymic = models.CharField('Отчество', max_length=155)
    phone = models.CharField('Номер телефона', max_length=155)
    email = models.EmailField('Email')
    passport = models.CharField("Паспортные данные", max_length=155)

    def get_FIO(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    

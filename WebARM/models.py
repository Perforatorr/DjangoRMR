from django.db import models

class RoleTypeChoices(models.TextChoices):
    MASTER = 'master', 'мастер'
    OPERATOR = 'operator', 'оператор'


class User(models.Model):
    rfid = models.AutoField(primary_key=True)
    name = models.CharField('first name', max_length=255)
    password = models.CharField('password',max_length=255)
    role = models.CharField(
        max_length=20,
        choices=RoleTypeChoices.choices,
        default=RoleTypeChoices.OPERATOR
        )


class Machine(models.Model):

    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField('name', max_length=255)
    condition = models.ForeignKey(
        'Condition',  # Ссылка на модель Condition
        related_name='machines',  # Опционально: обратная связь
        default = 0,
        on_delete = models.PROTECT

    )


class Condition(models.Model):

    id = models.IntegerField(primary_key=True)  
    name = models.CharField('name', max_length=255)


class ListChangeCondition(models.Model):

    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField()
    send = models.BooleanField()
    user = models.ForeignKey(
        'User',  # Ссылка на модель User
        related_name='userchange',  # Опционально: обратная связь
        on_delete = models.PROTECT
        )
    machine_id=models.ForeignKey(
        'Machine',  # Ссылка на модель Machine
        related_name='machinechange',
        on_delete = models.PROTECT
        )
    condition = models.ForeignKey(
        'Condition',  # Ссылка на модель Condition
        related_name='listchange', # Опционально: обратная связь
        on_delete = models.PROTECT 
        )

from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.utils.text import slugify


user = get_user_model()
class Condition(models.Model):
    id_number = models.CharField(max_length=13)
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"
    

class Machine(models.Model):
    name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=13, unique=True)
    code_number = models.CharField(max_length=13, unique=True)
    condition= models.ForeignKey(Condition, on_delete=models.CASCADE,null=True)
    critical_accident = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class UserMachine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE,unique=True)
    slug = models.SlugField(unique=True, blank=True)
    class Meta:
        unique_together = ('user', 'machine')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.machine.id_number)  # Генерация slug из заголовка
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.machine.name}"

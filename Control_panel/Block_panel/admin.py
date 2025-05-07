from django.contrib import admin
from .models import Machine,UserMachine,Condition

# Register your models here.

class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_number','code_number')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля, по которым будет происходить поиск
class UserMachineAdmin(admin.ModelAdmin):
    list_display = ('machine','user','condition')  # Поля, которые будут отображаться в списке
    search_fields = ('machine','user',)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('name','id_number')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)



admin.site.register(UserMachine, UserMachineAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Condition, ConditionAdmin)
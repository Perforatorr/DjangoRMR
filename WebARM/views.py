from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib import messages
from django.utils import timezone
from .models import User, Machine, ListChangeCondition, Condition
from functools import wraps
from django.http import HttpResponseRedirect


def login_auth(func):

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        return redirect('login')

    return wrapper

def login_view(request):
    title = "Вход в систему"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(name=username, password=password)
            request.session['user_id'] = user.rfid

            return redirect('panel')  # Замените на ваш роут
            
        except User.DoesNotExist:
            messages.error(request, "Неверные логин или пароль")
    
    return render(request, 'login.html', {'title': title})

@login_auth
def panel_view(request):
    machines = Machine.objects.all()
    if len(machines) == 1:
        pass
    return render(request, 'panel.html', {'machines': machines})

@login_auth
def change_condition_view(request, machine_id):
 
    machine = get_object_or_404(Machine, id=machine_id)
    conditions = Condition.objects.all()
    
    if request.method == 'POST':
        new_condition_id = request.POST.get('new_condition_id')
        
        try:
            # Получаем новое состояние
            new_condition = Condition.objects.get(id=new_condition_id)
            
            # Обновляем состояние машины
            machine.condition = new_condition
            machine.save()
            
            # Создаем запись об изменении состояния
            ListChangeCondition.objects.create(
                create_time=timezone.now(),
                send=False,
                user=User.objects.get(rfid=request.session['user_id']),
                machine_id=machine,
                condition=new_condition
            )
            
            messages.success(request, f"Состояние машины '{machine.name}' успешно изменено на '{new_condition.name}'")
            return redirect('panel')
            
        except Condition.DoesNotExist:
            messages.error(request, "Ошибка: выбранное состояние не существует")
    
    return render(request, 'change_condition.html', {
        'machine': machine,
        'conditions': conditions
    })

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    
    response = HttpResponseRedirect('/login/')
    response['Cache-Control'] = 'no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

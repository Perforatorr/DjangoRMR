from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import UserMachine,user ,Machine,Condition




@login_required(login_url='/auth/log/')
def index(request):  
    if request.method == 'POST':
        machines = request.POST.get('machine')
        condition = request.POST.get('options')
        mach = Machine.objects.filter(id_number = machines).get()
        user_machines = UserMachine.objects.filter(machine =mach)
        conndi = Condition.objects.filter(id_number =condition).get()
        for condition_machine in user_machines:
            condition_machine.condition = conndi
            condition_machine.save()
    template = 'index/index.html'
    current_user = request.user
    
    # Получаем все машины, связанные с текущим пользователем
    user_machines = UserMachine.objects.filter(user=current_user).select_related('machine','condition')
    machines = [user_machine for user_machine in user_machines]
    context = {'rect': machines}
    return render(request,template,context)


@login_required(login_url='/auth/log/')
def index2(request,condition, machines):
    mach = Machine.objects.filter(id_number = machines).get()
    user_machines = UserMachine.objects.filter(machine =mach)
    conndi = Condition.objects.filter(id_number =condition).get()
    for condition_machine in user_machines:
        condition_machine.condition = conndi
        condition_machine.save()
    return redirect('Block_panel:main')



@login_required(login_url='/auth/log/')
def change_condition(request,slug):    
    template = 'index/change.html'
    machine = UserMachine.objects.filter(slug=slug).get()
    if machine.condition.name == 'Эксплуатация':
        all_conditions = Condition.objects.all()
    else:
        all_conditions = Condition.objects.filter(id = 1 )
    
    context = {'all_conditions': all_conditions,'slug':slug}
    return render(request,template,context)




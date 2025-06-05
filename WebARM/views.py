from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def login_view(request):
    title = "Вход в систему"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(name=username, password=password)
            return redirect('dashboard')  # Замените на ваш роут
            
        except User.DoesNotExist:
            messages.error(request, "Неверные логин или пароль")
    
    return render(request, 'login.html', {'title': title})

def panel_view(request):
    data = [{'name':'Machine 1', 'condition':{'id':0}},{'name':'Machine 2', 'condition':{'id':1}},{'name':'Machine 3', 'condition':{'id':2}},{'name':'Machine 4', 'condition':{'id':0}}]
    return render(request, 'panel.html', {'machines': data})
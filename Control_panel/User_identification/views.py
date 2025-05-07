from django.shortcuts import render


from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy



class CustomLogoutView(LogoutView):
       # Убедитесь, что вы указали правильный путь для редиректа
       next_page = reverse_lazy('User_identification:log')  # Замените 'login' на ваш URL pattern

       # Если вы хотите использовать get_next_url
def logout(request):    
    pass


def log(request):    
    pass
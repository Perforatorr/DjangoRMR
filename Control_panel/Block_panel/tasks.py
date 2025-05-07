
def my_function():
    from django.contrib.sessions.models import Session
    Session.objects.all().delete()
    print("Функция вызвана")
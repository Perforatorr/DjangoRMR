from django.urls import path
from WebARM.api.views import *



urlpatterns = [
    path('api/machinenew/',MachineCreateView.as_view()),
    path('api/machinedel/',MachineDeleteView.as_view()),
    path('api/usernew/',UserCreatView.as_view()),
    path('api/userdel/',UserDeletedView.as_view()),

]
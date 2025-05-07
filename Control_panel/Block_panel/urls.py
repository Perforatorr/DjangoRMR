from django.urls import path
from . import views

app_name = 'Block_panel'

urlpatterns = [
    path('',views.index,name='main'),
    path('m/<slug:condition>/<slug:machines>/',views.index2,name='main2'),
    path('change_condition/<slug:slug>/',views.change_condition,name='change_condition'),
 
]

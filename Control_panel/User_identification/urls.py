from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


app_name = 'User_identification'

urlpatterns = [
    path('log/', LoginView.as_view(template_name='log/log.html'),name='log'),
    path('logout/',views.CustomLogoutView.as_view(template_name='index/block.html'),name='logout'),
    
]
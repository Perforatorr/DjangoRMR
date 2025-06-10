from django.contrib import admin
from django.urls import include, path
from WebARM.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('WebARM.api.urls')),
    path('login/', login_view, name='login'),
    path('panel/', panel_view, name ='panel'),
    path('panel/machine/<str:machine_id>/change_condition/', change_condition_view, name='change_condition'),
    path('logout/', logout_view, name ='logout'),
    path('panel/logout/', logout_view, name ='logout'),
    ]
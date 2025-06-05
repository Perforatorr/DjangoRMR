from django.contrib import admin
from django.urls import include, path
from WebARM.views import login_view, panel_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('WebARM.api.urls')),
    path('login/', login_view, name='login'),
    path('panel/', panel_view, name ='panel')

]
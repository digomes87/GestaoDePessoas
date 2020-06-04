from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('apps.core.urls'), name="core"),
    path('funcionarios/', include('apps.funcionarios.urls'), name="funcionarios"),
    path('empresa/', include('apps.empresas.urls'), name="empresas"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]

from apps.empresas.views import EmpresaCreate, EmpresaEdit
from django.urls import path


urlpatterns = [
    path('novo/', EmpresaCreate.as_view(), name="nova-empresa"),
    path('editar/<int:pk>', EmpresaEdit.as_view(), name="edit-empresa"),
]
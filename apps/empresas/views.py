from django.views.generic.edit import CreateView, UpdateView
from apps.empresas.models import Empresa
from django.http import HttpResponse


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionarios
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
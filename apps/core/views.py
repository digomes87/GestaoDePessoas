from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.funcionarios.models import Funcionarios


class Home(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = ('core/index.html')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user
        print(context['usuario'])
        return context



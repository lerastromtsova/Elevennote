from django.contrib.auth import authenticate, login
from django.views.generic import FormView

from .forms import UserCreationForm


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)

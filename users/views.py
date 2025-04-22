from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            'Welcome to SkyStore!',
            'Thank you for registering.',
            settings.DEFAULT_FROM_EMAIL,
            [form.instance.email],
            fail_silently=False,
        )
        return response


class EmailLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'users/login.html'


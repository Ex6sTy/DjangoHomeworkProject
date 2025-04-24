from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView
from .forms import LoginForm, ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
import secrets
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import HttpResponse


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # пользователь неактивен до подтверждения почты
        user.activation_token = secrets.token_urlsafe(32)
        user.save()
        activation_link = self.request.build_absolute_uri(
            reverse('activate', kwargs={'token': user.activation_token})
        )
        send_mail(
            'Подтвердите регистрацию на SkyStore',
            f'Для активации аккаунта перейдите по ссылке:\n{activation_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileEditForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('edit_profile')

    def get_object(self):
        return self.request.user


def activate(request, token):
    User = get_user_model()
    try:
        user = User.objects.get(activation_token=token)
        user.is_active = True
        user.activation_token = None
        user.save()
        return HttpResponse("Аккаунт успешно подтверждён! Теперь вы можете войти.")
    except User.DoesNotExist:
        return HttpResponse("Ссылка недействительна или уже использована.")
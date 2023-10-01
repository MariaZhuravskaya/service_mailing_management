from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import RegisterCreationForm, ProfileChangeForm
from users.models import User


class RegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = RegisterCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Подтверждение e-mail"""
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            # генерация токена
            user.id = User.objects.make_random_password()
            user.set_password(user.id)
            user.save()

            send_mail(
                'Подтвердите свой электронный адрес',
                f"Ваша учетная запись подтверждена!"
                f"Перейтите по ссылке - http://127.0.0.1:8000/users/verify/{user.id}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
        return super().form_valid(form)


class ProfileView(UpdateView):
    """Изменение профиля"""
    model = User
    form_class = ProfileChangeForm
    success_url = reverse_lazy('users:login')


class UserPassword(View):
    """Восстановление пароля"""
    model = User
    success_url = reverse_lazy('users:login')
    template_name = 'users/password_reset_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        try:

            email = request.POST.get('email')
            user = User.objects.get(email=email)

            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()

            # Функционал для отправки письма
            send_mail(
                'Ваш пароль',
                f"Ваш новый пароль! - {password}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse_lazy('users:login'))

        except ObjectDoesNotExist:
            print("Объект не сушествует")
        except MultipleObjectsReturned:
            print("Найдено более одного объекта")


class UserVerifyView(View):
    model = User
    success_url = reverse_lazy('users:login')
    template_name = 'users/check_email.html'

    def verify(self, request, id_user):
        user = User.objects.get(id=id_user)

        if user is not None and user.id == id_user:
            user.is_active = True
            user.save()
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect(reverse_lazy('users:login'))



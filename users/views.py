from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView

from users.forms import RegisterCreationForm, ProfileChangeForm
from users.models import User


class UserLoginView(LoginView):
    ""


class RegisterView(CreateView):
    model = User
    form_class = RegisterCreationForm
    template_name = 'users/register.html'


class ProfileView(UpdateView):
    model = User
    form_class = ProfileChangeForm
    template_name = 'users/profile.html'

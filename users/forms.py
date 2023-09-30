from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class RegisterCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'cantry')

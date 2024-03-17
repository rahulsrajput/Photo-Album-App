from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class customLogin(AuthenticationForm):
    pass
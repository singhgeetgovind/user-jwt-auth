from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ModelForm,Form

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1','password2','address']

class SignInForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email','password']

class EditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name', 'last_name','address']




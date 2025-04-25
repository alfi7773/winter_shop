from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'inputbox', 'placeholder' : 'username'}),
             'email': forms.EmailInput(attrs={'class': 'inputbox', 'placeholder' : 'email'}),
             'first_name' : forms.TextInput(attrs={'class': 'inputbox', 'placeholder':'first_name'}),
             'last_name' : forms.TextInput(attrs={'class': 'inputbox', 'placeholder':'last_name'}),
             'password1' : forms.PasswordInput(attrs={'class': 'inputbox', 'placeholder':'password1'}),
             'password2' : forms.PasswordInput(attrs={'class': 'inputbox', 'placeholder':'password2'})
        } 
        
        
            
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True
            self.fields['email'].required = True
            
            # self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'inputbox',  'placeholder': 'password1'})
            # self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'inputbox', 'placeholder': 'password2'})
            
            
class LoginForm(forms.Form):
    username = forms.CharField(label='имя пользователя', widget=forms.TextInput(attrs={
        'class': 'inputbox', 'placeholder': 'username'
    }))

    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={
        'class': 'inputbox', 'placeholder': 'password'
    }))
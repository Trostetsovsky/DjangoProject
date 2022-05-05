from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        psw_list = self.cleaned_data
        print(psw_list)
        if psw_list['password'] != psw_list['password2']:
            raise forms.ValidationError('Пароли не совпалЫ.')
        return psw_list['password']

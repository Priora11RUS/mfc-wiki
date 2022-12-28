from django import forms
from django.forms import ClearableFileInput
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

# Добавляем класса формы, описывающую форму добавления статьи
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Введите заголовок статьи'
             })
        self.fields["slug"].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Укажите url адрес'
             })
        self.fields["file"].widget.attrs.update({
            'class': 'form-control',
            'multiple': True
             })
    class Meta:   
        model = Post
        fields = ['title', 'slug', 'content', 'file']
        

# Собственный валидатор
    def clean_title(self): # Пишем clean и название формы
        title = self.cleaned_data['title'] # Получение данных по заголовку
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов') # Вывод ошибки
        return title

# Добавляем класса формы, описывающую форму регистрации
class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'name':'username',
            'id':'username',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Имя пользователя'
             })
        self.fields["email"].widget.attrs.update({
            'name':'email',
            'id':'email',
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Почтовый адрес'
             })
        self.fields["password1"].widget.attrs.update({
            'name':'password1',
            'id':'password1',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Введите пароль'
             })
        self.fields["password2"].widget.attrs.update({
            'name':'password2',
            'id':'password2',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Повторите пароль'
        })
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'name':'username',
            'id':'username',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Имя пользователя'
             })
        self.fields["password"].widget.attrs.update({
            'name':'password',
            'id':'password',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Пароль'
        })


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields, models

from django import forms
from django.contrib.auth.models import User

from todo.models import Task

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control m-2',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control m-2',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control m-2',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control m-2',
    }))

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))

    class Meta:
        model = User
        fields = '__all__'


#   <p>User : {{ task_form.user }}</p>
#                                 <p>Title : {{ task_form.title }}</p>
#                                 <p>when_to_do : {{ task_form.when_to_do }}</p>
#                                 <p>Email : {{ task_form.email }}</p>
#                                 <p>Completed : {{ task_form.completed }}</p>

class TaskForm(forms.ModelForm):
    # CHOICES = (
    #     ('ser',)*2,
    #     ('kser',)*2,
    # )
    title = forms.CharField(widget=forms.TextInput( attrs={
        'class':'form-control',
        'placeholder':'Enter what to do ...'
    }))

    when_to_do = forms.CharField(widget=forms.TextInput( attrs={
        'class':'form-control',
        'placeholder':'year-month-day'
    }))
    class Meta:
        model = Task
        exclude = ('user', 'email')

class EditForm(forms.ModelForm):
    # CHOICES = (
    #     ('ser',)*2,
    #     ('kser',)*2,
    # )
    title = forms.CharField(widget=forms.TextInput( attrs={
        'class':'form-control',
        'placeholder':'Update what to do ...'
    }))

    when_to_do = forms.CharField(widget=forms.SelectDateWidget( attrs={
        'class':'form-control',
        'placeholder':'year-month-day'
    }))

    email = forms.CharField(widget=forms.TextInput( attrs={
        'class':'form-control',
        'placeholder':'Email',
    }))

    # completed = forms.CharField(widget=forms.ChoiceWidget( attrs={
    #     'class':'form-control',
    # }))
  
    class Meta:
        model = Task
        exclude = ('user',)
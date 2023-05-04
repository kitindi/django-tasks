from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


"""
User Registration
- username
- email
- password
- confirm

User Login

- username
- password

"""

class UserRegistrationForm(UserCreationForm):
     
     def __init__(self, *args, **kwargs):
          super(UserRegistrationForm, self).__init__(*args, **kwargs)
          self.fields['username'].widget.attrs.update({'class': 'w-full p-2 outline-none border-2 border-slate-200'})
          self.fields['email'].widget.attrs.update({'class': 'w-full p-2 outline-none border-2 border-slate-200'})
          self.fields['password1'].widget.attrs.update({'class': 'w-full p-2 outline-none border-2 border-slate-200'})
          self.fields['password2'].widget.attrs.update({'class': 'w-full p-2 outline-none border-2 border-slate-200'})
          
     class Meta:
          model = User
          fields = ['username', 'email', 'password1', 'password2']

# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200 '}), required= True)
#     email = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'})) 
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'}))
#     confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'}))

class UserLoginForm(forms.Form):
     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'}))


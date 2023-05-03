from django import forms


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

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200 '}), required= True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'})) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'}))
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'}))

class UserLoginForm(forms.Form):
     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 outline-none border-2 border-slate-200'}))


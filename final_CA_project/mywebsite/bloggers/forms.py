from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Please enter your username'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Please enter your password'
        })

    class Meta:
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Please enter your username'
        })

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Please enter your first name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Please enter your last name'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Please enter your email address'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Please enter your password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'placeholder': 'Please confirm your password'
        })
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 
    'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 
    'placeholder': 'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 
    'placeholder': 'Confirm New Password'}))
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']

class EditUserProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 
    'placeholder': "Please enter your email"}))

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
    'placeholder': "Please enter your first name"}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
    'placeholder': "Please enter your last name"}))

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 
    'placeholder': "Please enter your username"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
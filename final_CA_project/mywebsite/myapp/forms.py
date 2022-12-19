from tkinter import Widget
from django import forms
from .models import Contact, Blog, Blogcomment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            "e_mail": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email address'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
            "contact_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your message here'}),
        }

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('post_date', 'slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'})
        }

class CommentBlogForm(forms.ModelForm):

    class Meta:
        model = Blogcomment
        fields = "__all__"

        widgets = {
            'author': forms.TextInput(attrs={'value':'', 'id':'author', 'type':'hidden'}),
            'blog': forms.TextInput(attrs={'value':'', 'id':'blog', 'type':'hidden'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

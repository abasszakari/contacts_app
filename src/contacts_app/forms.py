from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname','organization','position','mobile','address']
        labels = {'fullname': 'Full Name'}
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['organization'].required = False
        self.fields['position'].required = False
        self.fields['address'].required = False

class CreateUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {'fullname': 'Full Name'}
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['organization'].required = False
        self.fields['position'].required = False
        self.fields['address'].required = False

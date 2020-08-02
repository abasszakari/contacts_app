from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact

def contact_list(request):
    contact_list = Contact.objects.all()
    context = {"contact_list": contact_list}
    return render(request, 'contacts_app/contact_list.html', context)

def contact_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ContactForm()
        else:
            contact = Contact.objects.get(pk=id)
            form = ContactForm(instance=contact)
        context = {'form': form}
        return render(request, 'contacts_app/contact_form.html', context)
    else:
        if id == 0:
            form = ContactForm(request.POST)
        else:
            contact = Contact.objects.get(pk=id)
            form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        return redirect('contacts_app:contact_list')

def contact_delete(request, id):
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect('contacts_app:contact_list')

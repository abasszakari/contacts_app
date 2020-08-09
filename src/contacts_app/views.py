from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .forms import ContactForm, CreateUserForm
from .filters import ContactFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Contact

def register(request):
    if request.user.is_authenticated:
        return redirect('contacts_app:contact_list')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was successfully created for ' + user)
                return redirect('contacts_app:login')
        context = {
            'form': form
        }
        return render(request, 'contacts_app/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('contacts_app:contact_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(user.id)
                login(request, user)
                return redirect('contacts_app:contact_list')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'contacts_app/login.html')
        return render(request, 'contacts_app/login.html')

@login_required(login_url='contacts_app:login')
def logoutUser(request):
    logout(request)
    return redirect('contacts_app:login')

@login_required(login_url='contacts_app:login')
def contact_list(request):
    contact_list = Contact.objects.filter(user=request.user)
    my_filter = ContactFilter(request.GET, queryset=contact_list)
    contact_list = my_filter.qs
    context = {"contact_list": contact_list, 'my_filter':my_filter}
    return render(request, 'contacts_app/contact_list.html', context)

@login_required(login_url='contacts_app:login')
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
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect('contacts_app:contact_list')

@login_required(login_url='contacts_app:login')
def contact_delete(request, id):
    contact = Contact.objects.get(pk=id)
    contact.delete()
    return redirect('contacts_app:contact_list')

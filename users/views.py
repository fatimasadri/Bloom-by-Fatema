from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def login_user(request):
    msg = None
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
         login(request, user)
         return redirect('/')
         msg = " User login successfully"

       else:
         msg="Invalid Credentials"
         messages.success(request, ("there was an error logging in, try again!"))
         return redirect('login')

    else:
     dic={'msg': msg}
     return render(request, 'registration/login.html', dic, {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were successfully loged out"))
    return redirect('/')

def register_user(request):
    msg = None
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = form.cleaned_data['cpwd']
            contact = form.cleaned_data['mobile']
            image = form.cleaned_data['image']
            address = form.cleaned_data['address']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("Registration successful"))
            return redirect('/')
            msg = " User registered successfully"
        else:
            form = UserCreationForm()
            msg="Invalid Credentials"
    return render(request, 'registration/register.html', {
    'form':form,
    })

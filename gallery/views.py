
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from gallery.models import Gallery, Comment, UserProfile, User, Customer
from django.contrib.auth import authenticate,login
from gallery.models import UserProfile
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *
#from .forms import CheckoutForm

# Create your views here.
def home(request):
    return render(request, 'gallery/home.html')

def shop(request):
    return render(request, 'gallery/shop.html')


def contactus(request):
    return render(request, 'gallery/contactus.html')

def cart(request):
    return render(request,'gallery/cart.html')

def signin(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            if user.is_staff:
                login(request, user)
                msg = "User login successfully"
            else:
                msg = "Invalid Credentials"
        except:
            msg = "Invalid Credentials"
    dic = {'msg': msg}
    return render (request, 'gallery/signin.html', dic)

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        image = request.FILES['image']
        user = User.objects.create_user(user=email, first_name=fname, last_name=lname, email=email, password=password)
        UserProfile.objects.create(user=user, mobile=mobile, image=image)
        messages.success(request, "Registration Successful")
    return render(request, 'gallery/signup.html', locals())


#class CheckoutView(request):
#    def get(self, *args, **kwargs):
#        #form
#        form = CheckoutForm()
#        context = {
#         'form': form
#        }
#        return render(request, "gallery/cart.html", context )

#    def post(self, *args, **kwargs):
#        form = CheckoutForm(self.request.POST or None)
#        if form.is_Valid():
#            print("The form is valid")
#            return redirect("/")

#class CheckoutView(generic.CreateView):
    #form_class = CheckoutForm
    #template_name = 'gallery/cart.html'
    #success_url = reverse_lazy('cart')

#class shop(request):
#    products = Product.objects.all()
#    context = {'products':products}
#    return render(request, 'gallery/shop',context)

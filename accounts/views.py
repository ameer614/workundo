from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

from .forms import Create_New_user


# Create your views here.


class RegisterView(FormView):
    template_name = "accounts/login.html"
    form_class = Create_New_user

    def form_valid(self, form):
        user = form.save()
        return redirect("posts:home")


def login_view(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(email=email,password=password)

        if user:
            login(request,user)
            return redirect("posts:home")
        else:
            return render(request,'accounts/loginn.html', {'error':True}) 
    return render(request,'accounts/loginn.html')



def base(request):
    return render(request,'base.html')

def cust_h(request):
    return render(request,'accounts/base.html')

def page_not_found_view(request, exception):
    return render(request, "error404.html", {})

def logout_view(request):
    logout(request)
    return redirect("accounts:register")

def base(request):
    return render(request,'accounts/log.html')

def home(request):
    return render(request,'accounts/index.html')


from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth import get_user_model
# Create your views here.

def home(request):
    return render(request,'home.html')

def pcod(request):
    return render(request,'data/pcod.html')

def aub(request):
    return render(request,'data/aub.html')

class RegisterView(SuccessMessageMixin, CreateView):

    template_name = 'register.html'
    form_class = RegisterForm
    success_message = "%(username)s Registered Successfully"
    model = get_user_model()

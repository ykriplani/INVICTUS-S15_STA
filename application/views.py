from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import RegisterForm,ContactForm
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def pcod(request):
    return render(request,'data/pcod.html')

def aub(request):
    return render(request,'data/aub.html')

def about(request):
    return render(request,'data/about.html')



def contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request,f"{post.first_name} your form is submitted successfully. We will contact you shortly!!!")
            return redirect ("home")
        # return HttpResponse(post.title)
        messages.error(request,f"Error!!!!")
  
    form = ContactForm()

    context = {
        'form': form,
        'page':'contact',
    }
    return render(request, "data/contact.html", context)


class RegisterView(SuccessMessageMixin, CreateView):

    template_name = 'register.html'
    form_class = RegisterForm
    success_message = "%(username)s Registered Successfully"
    model = get_user_model()



from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf


# Create your views here.
from .forms import SingUpForm

def home(request):
    
    form = SingUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'We will in touch')
        return  HttpResponseRedirect('/thank-you/')
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

def thankyou(request):
    
    
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def about(request):
    
    
    return render_to_response("about.html",
                              locals(),
                              context_instance=RequestContext(request))


def my_view(request):
    form = SingUpForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return  HttpResponseRedirect('/welcome/') 
        else:
            return HttpResponseRedirect('/failed/')
    
        
def welcome(request):
    
    
    return render_to_response("welcome.html",
                              locals(),
                              context_instance=RequestContext(request))

def failed(request):
    
    
    return render_to_response("failed.html",
                              locals(),
                              context_instance=RequestContext(request))

                    
    
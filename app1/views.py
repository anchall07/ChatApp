from django.contrib.auth import login

from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.

def front_page(request):
    return render (request , 'app1/front_page.html')

def signup(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            return redirect('frontpage')

    else:
        form = SignUpForm()

    return render(request, 'app1/signup.html',{'form':form})
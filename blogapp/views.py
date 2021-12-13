from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import OrderForm, CreateUserForm
from django.contrib import messages
from .forms import OrderForm, CreateUserForm, CustomerForm


def index(request):

    posts = Post.objects.all()
    data = {
        'posts': posts
    }
    return render(request, "blogapp/index.html", data)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'La cuenta fue creada por ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, "register.html", context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, "login.html", context)


def userPage(request):
    context = {}
    return render(request, 'user.html', context)


def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'account_settings.html', context)


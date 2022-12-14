
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm


from .models import *
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    
    return render(request, 'login.html')

    
def signup(request):
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' +user)
            return redirect('login')
        else:
            messages.info(request, "please enther correct information and enter the unique username and strong password")


    form = CreateUserForm()
    context={'form': form}
    return render(request, 'signup.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def breakfast(request):
    food = Food.objects.filter(category = 'breakfast')
    context = {
        'foods': food
    }
    return render(request, 'breakfast.html', context)

@login_required(login_url='login')
def lunch(request):
    food = Food.objects.filter(category = 'lunch')
    context = {
        'foods': food
    }
    return render(request, 'lunch.html', context)

@login_required(login_url='login')
def dinner(request):
    food = Food.objects.filter(category = 'dinner')
    context = {
        'foods': food
    }
    return render(request, 'supper.html', context)


@login_required(login_url='login')
def order(request, pk):
    if request.method == 'GET':
            food = Food.objects.get(id = pk)
            quantity = request.GET.get('quanitiy')
            print(quantity)
            order = Order(user = request.user,  category=food.category, food=food.image)
            order.save()
            return redirect('home')


@login_required(login_url='login')
def orderpage(request, pk):
    food = Food.objects.get(id = pk)
    if request.method == 'POST':
            food = Food.objects.get(id = pk)
            quantity = request.POST.get('quanitiy')
            order = Order(user = request.user,  category=food.category, food=food.image, quantity=quantity)
            order.save()
            return redirect('home')
    context = {
        'food': food
    }
    return render(request, 'orderpage.html', context)


@login_required(login_url='login')
def adminpage(request):
    order = Order.objects.all()
    context = {
        "orders" : order
    }
    return render(request, 'adminpage.html', context)

@login_required(login_url='login')
def singleorder(request):
    order = Order.objects.filter(user = request.user)
    context = {
        "orders" : order
    }
    return render(request, 'orders.html', context)


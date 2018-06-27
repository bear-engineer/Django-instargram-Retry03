from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignupForm


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('users:sign-in')
    else:
        return render(request, 'sign/sign_in.html')

def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():

            user = sign_up()
            login(request, user)
            return redirect('index')

    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'sign/sign_up.html', context)
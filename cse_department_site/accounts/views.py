from django.shortcuts import render
from django.shortcuts import redirect
from .models import User, StudentProfile, StaffProfile, AlumniProfile
from django.views.generic import CreateView
from .forms import CreateUserForm
from django.contrib.auth import autheticate,login, logout,register 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
def register(request):
    if request.method == 'POST':
        form= CustomUserCreationForm(request.POST)
        if form. is_valid  ():
            user= form.save()
            login(request, user)
            return redirect('home')


    else:
        form= CustomUserCreationForm()
    return render(request, 'accountregister.html', {'form': form})


                



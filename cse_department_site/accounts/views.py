from django.shortcuts import render
from django.shortcuts import redirect
from .models import User, StudentProfile, StaffProfile, AlumniProfile
from django.views.generic import CreateView
from .forms import CreateUserForm
from django.contrib.auth import autheticate,login, logout,register 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_page (request):
    if register.user.is_authenticated:
        return redirect('home')
    

    else:
        form = CreateUserForm()
        if request.method =='POST':
            form= CreateUserForm(request.POST)
            if form.is_valid:
                form.save()
                user= form.cleaned_data.get('username')

                messages.success(request, 'account was created for'+ user)

                return redirect('home')
            
            return render(request, 'auth/registe.html', context ={'form': form})
        

def login_page(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if request.method =='POST':
                username= request.POST.get('username')
                password= request.POST.get('password')

                user= autheticate(request, username=username, password=password)

            if user is not None: 
                    login(request, user)
                    return redirect ('home')
                
            else:
                messages.info(request, 'Username or passsword is incorrect')

                return render(request, 'auth/login.html')
            
def logoutUser(request):
     logout(request)
     messages.info(request, "you have successfully logged out")
     return redirect('login')
            

                



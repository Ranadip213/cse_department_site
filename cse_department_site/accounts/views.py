from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import AlumniForm, CreateUserForm, StaffForm, StudentForm
from django.contrib import messages

def register_page(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # Redirect to home page if the user is already logged in
        return redirect('home')
    else:
        # Create an instance of the CreateUserForm
        form = CreateUserForm()
        if request.method == 'POST':
            # Populate the form with data from the request
            form = CreateUserForm(request.POST)
            if form.is_valid():
                # Save the form and create a new user
                user = form.save()
                login(request, user)  # Log in the user after registration
                # Get the user type from the form data
                user_type = form.cleaned_data.get('user_type')

                # Redirect to the appropriate form based on user type
                if user_type == 'student':
                    return redirect('register_student')
                elif user_type == 'alumni':
                    return redirect('register_alumni')
                elif user_type == 'staff':
                    return redirect('register_staff')
                
        # Render the register template with the form
        return render(request, 'components/register.html', context={'form': form})         

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'components/student_form.html', context={'form': form})

def alumni_form(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            alumni = form.save(commit=False)
            alumni.user = request.user
            alumni.save()
            return redirect('home')
    else:
        form = AlumniForm()
    return render(request, 'components/alumni_form.html', context={'form': form})

def staff_form(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.user = request.user
            staff.save()
            return redirect('home')
    else:
        form = StaffForm()
    return render(request, 'components/staff_form.html', context={'form': form})

def login_page(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # If yes, redirect the user to the home page
        return redirect('home')
    else:
        # If the request method is 'POST'
        if request.method == 'POST':
            # Get the username and password from the request
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Attempt to authenticate the user using the provided credentials
            user = authenticate(request, username=username, password=password)

            # If authentication is successful
            if user is not None:
                # Log the user in and redirect them to the home page
                login(request, user)
                return redirect('home')
            else:
                # If authentication failed, display a message to the user
                messages.info(request, 'Username OR password is incorrect')

        # If the request method is not 'POST', render the login page
        return render(request, 'components/login.html')
    
def logoutUser(request):
    """
    Logs out the current user and redirects them to the login page
    """
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('home')

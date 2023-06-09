from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
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
                form.save()
                # Get the username of the newly created user
                user = form.cleaned_data.get('username')
                # Send a success message
                messages.success(request, 'Account was created for ' + user)
                # Redirect to the home page
                return redirect('home')
        # Render the register template with the form
        return render(request, 'components/register.html', context={'form': form})         

def logoutUser(request):
    """
    Logs out the current user and redirects them to the login page
    """
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('home')

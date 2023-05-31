from django.shortcuts import render
from django.shortcuts import redirect
from .models import User, StudentProfile, StaffProfile, AlumniProfile
from django.views.generic import CreateView
from .forms import StudentProfileSignUpForm,StaffProfileSignUpForm, AlumniProfileSignUpForm
# Create your views here.
def index(request):
    return render(request,'index.html')
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentProfileSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('index')
class StaffSignUpView(CreateView):
    model = User
    form_class = StaffProfileSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('index')
    
class alumniSignUpView(CreateView):
    model = User
    form_class = AlumniProfileSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('index')

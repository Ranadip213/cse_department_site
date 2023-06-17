from django.shortcuts import render

from about.models import Club

# Create your views here.
def homePage(request):
    clubs = Club.objects.all()
    context = {'clubs':clubs}
    return render(request,'screens/home.html', context)
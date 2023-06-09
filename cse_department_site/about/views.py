from django.shortcuts import render

from django . shortcuts import render
from .models import Gallery

def carousel_images(request):
    data = Gallery.objects.all()[:6]
    context = {'images': data}
    return render(request, 'components/carousel.html',context)

def gallery_images(request):
    data = Gallery.object.all()
    context = {'images': data}
    return render(request,'screens/gallery.html', context)
    
def clubs(request):
    return render(request, 'screens/clubs.html')
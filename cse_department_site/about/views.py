from django.shortcuts import render

# Create your views here.

from django . shortcuts import render
from .models import Gallery

def carousel_images(request):
    data = Gallery.objects.all()[:6]
    context = {'images': data}
    return render(request, 'carousel.html',context)

def gallery_images(request):
    data = Gallery.object.all()
    context = {'images:' data}
    return render{request,'gallery.html', context} 
    

from django.shortcuts import render
from .models import Club, Gallery

from accounts.models import Student, Staff, Alumni


def carousel_images(request):
    """
    Retrieves the latest 6 gallery images for the carousel.
    Renders the 'carousel.html' template with the retrieved images.
    """
    data = Gallery.objects.all()[:6]
    context = {'images': data}
    return render(request, 'components/carousel.html', context)


def gallery_images(request):
    """
    Retrieves all gallery images.
    Renders the 'gallery.html' template with the retrieved images.
    """
    images = Gallery.objects.all()
    context = {'images': images}
    return render(request, 'screens/gallery.html', context)


def student(request):
    data = Student.objects.all()
    context = {"students": data}
    return render(request, 'screens/student.html', context)


def facalty(request):
    data = Student.objects.all()
    context = {"facaltys": data}
    return render(request, 'screens/facalty.html', context)


def alumai(request):
    data = Alumni.objects.all()
    context = {"alumais": data}
    return render(request, 'screens/alumai.html', context)
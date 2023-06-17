from django.shortcuts import render
from .models import Club, Gallery

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

def clubes_page(request):
    """
    Retrieves all clubs.
    Renders the 'clubs.html' template with the retrieved clubs.
    """
    clubs = Club.objects.all()
    context = {'clubs':clubs}
    return render(request, 'components/clubs_pages.html', context)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Image
from base.models import Information

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    infos = Information.objects.all()
    info = infos[0]
    return render(request, 'albums/albums.html', {'albums': albums, 'info': info})

def album(request, name):
    imgs = Image.objects.filter(album_name__name=name)
    infos = Information.objects.all()
    info = infos[0]
    name = imgs[0].album_name.name
    return render(request, 'albums/images.html', {'images': imgs, 'info': info, 'name': name})

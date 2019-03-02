from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Information
from albumns.models import Cover, Album

# Create your views here.
def index(request):
    infos = Information.objects.all()
    info = infos[0]
    services = Service.objects.all()
    albums = Album.objects.all()
    return render(request, 'base/index.html', {'info': info, 'services': services, 'albums': albums})

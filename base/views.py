from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Information

# Create your views here.
def index(request):
    infos = Information.objects.all()
    info = infos[0]
    services = Service.objects.all()
    return render(request, 'base/index.html', {'info': info, 'services': services})

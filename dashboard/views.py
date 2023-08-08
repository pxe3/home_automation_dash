from django.shortcuts import render
from .models import SmartLight
from .models import SmartFan

# Create your views here.

def smart_lights(request):
    lights = SmartLight.objects.all()
    return render(request, 'dashboard/smart_lights.html', {'lights': lights})


def smart_fans(request):
    fans = SmartFan.objects.all()
    return render(request, 'dashboard/smart_fans.html', {'fans': fans})
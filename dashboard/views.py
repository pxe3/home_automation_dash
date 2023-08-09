from django.shortcuts import render
from .models import SmartLight
from .models import SmartFan
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Simulated smart switch status (True for on, False for off)
smart_switch_status = False

@api_view(['POST'])
def control_smart_switch(request):
    global smart_switch_status

    if request.method == 'POST':
        command = request.data.get('command')

        if command == 'toggle':
            smart_switch_status = not smart_switch_status
            status_text = 'on' if smart_switch_status else 'off'
            response_data = {
                'status': smart_switch_status,
                'message': f'Smart switch turned {status_text}.'
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid command.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)
    
    
def smart_lights(request):
    lights = SmartLight.objects.all()
    return render(request, 'dashboard/smart_lights.html', {'lights': lights})

def home(request):
    return render(request, 'dashboard/home.html')


def smart_fans(request):
    fans = SmartFan.objects.all()
    return render(request, 'dashboard/smart_fans.html', {'fans': fans})
from django.shortcuts import render
from main.models import *

def mainpage(http_request):
  context = {
    'updates': list(Update.objects.all().order_by('-id')[:10])
  }
  return render(http_request, 'main/mainpage.html', context)

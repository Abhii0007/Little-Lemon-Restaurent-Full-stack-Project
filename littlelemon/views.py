from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    try:
        return render(request, 'home.html')
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
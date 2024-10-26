from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
def home(request):
    return HttpResponse('this is first project_1')

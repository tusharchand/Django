from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('0123456789')
    special_char = list('`~-_=+[{]}\|;:\'",<.>/?!@#$%^&*()')
    generated_pass = ''
    
    if request.GET.get('uppercase'):
        uppercase_char = [x.upper() for x in characters]
        characters.extend(uppercase_char)
    
    if request.GET.get('numbers'):
        characters.extend(numbers)
    
    if request.GET.get('specialchar'):
        characters.extend(special_char)
    
    length = int(request.GET.get('length', 12))
    
    for i in range(length):
        generated_pass += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': generated_pass})

def about(request):
    return render(request, 'generator/about.html')
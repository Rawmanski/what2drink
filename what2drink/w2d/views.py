from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.


def index(request):
    query = "margarita"
    response =  requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+query+"")
    jsonResponse = response.json()
    drinks = jsonResponse['drinks']
    return render(request, 'w2d/index.html', {'drinks':drinks})

def search(request):
    if request.method == "POST":
        userText = request.POST.get('userText')
        response =  requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+userText+"")
        jsonResponse = response.json()
        drinks = jsonResponse['drinks']
        return render(request, 'w2d/index.html', {'drinks':drinks})
    else:
        return render(request, "w2d/index.html")

def about(request):
    return render(request, 'w2d/about.html')

def contact(request):
    return render(request, 'w2d/contact.html')

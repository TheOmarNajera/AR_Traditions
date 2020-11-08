from django.shortcuts import render, HttpResponse, redirect
import requests
"""
import cgi
print "Content-Type: text/html\n\n"
my_form = cgi.FieldStorage()for name in my_form.keys():
print "Input: " + name + " value: " + cgi.escape(my_form[name].value) + "<BR>"
"""

# Create your views here.7

def index(request):
    return render(request, 'index.html')

def AR_Camera(request):
    return render(request, 'RvEjercice.html')

def hola_mundo(request):
    if request.method == 'POST':
        title = request.POST['title']
        search_term = title

        subscription_key = "0f1d040c12654561b65af149b116f2c8"
        search_url = "https://api.bing.microsoft.com/v7.0/images/search"

        headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

        params  = {"q": search_term, "license": "any", "imageType": "photo"}

        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:30]]

        n = thumbnail_urls

        return render(request,'hola.html',{
            'Imagenes': n
        })


def buscador(request):
    return render(request,'buscador.html')
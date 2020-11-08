from django.shortcuts import render, HttpResponse, redirect
import requests
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

prediction_key = '19208769e9464095adc110aa4b6fcc99'
ENDPOINT = 'https://southcentralus.api.cognitive.microsoft.com/'
project_id = 'e79751a3-4025-45d1-bc40-12d08eb8b930'
publish_iteration_name = 'Iteration5'
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

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
        thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:1]]
        
        

        n = thumbnail_urls

        result = []
        predictions = []

        for i in n:
            results = predictor.classify_image_url(project_id, publish_iteration_name, i)
            for prediction in results.predictions:
                predictions.append(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
            result.append(predictions)
        print(result)

        return render(request,'hola.html',{
            'Imagenes': n,
            'Datas' : result
        })


def buscador(request):
    return render(request,'buscador.html')

def predicciones(request):
    try:
        if request.method == 'POST':
            title = request.POST['imagen1']
            print(title)
        return redirect('index')
    except:
        return HttpResponse("Hola mundo")

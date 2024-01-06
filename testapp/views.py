from django.shortcuts import render
import json 
import requests

# Create your views here.
def home(request):
    if request.method=='POST':
        query = request.POST['search']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        response = requests.get(api_url+query, headers={'X-Api-Key': 'Kb8Z0MJyEw0aImzxSnpYLw==PVc44I7EEcL5n4Pb'})
        try:
            api=json.loads(response.content)
        except :
            api="oohhh ! something went wrong, try again"
        return render(request,'testapp/home.html',{'api':api})
    else:
        return render (request,'testapp/home.html',{'query':'Enter a valid food name'})
from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
def index(request):
    information = {"name":"index"}
    return render(request, "index.html", information)

def tomato_view(request):
    context = {}
    if request.method == 'POST':
        # Extract the data directly from POST and add it to the context
        context['tomato_name'] = request.POST.get('tomato_name', '')
        context['tomato_description'] = request.POST.get('tomato_description', '')
        context['tomato_number'] = request.POST.get('tomato_number', 0)
        context['is_tomato'] = request.POST.get('is_tomato', 'off') == 'on'
    
    return render(request, 'tomato.html', context)

def variables_view(request):
    # Define the base URL for the API
    base_url = "https://us.rest.logs.insight.rapid7.com/query/variables"
    
    # Define the headers using API key from settings
    headers = {
        'x-api-key': settings.RAPID7_API_KEY,
        'Content-Type': 'application/json',
    }
    
    # Make the API call
    response = requests.get(base_url, headers=headers)
    variables = response.json()
    
    return render(request, 'variables.html', {'variables': variables})
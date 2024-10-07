from django.shortcuts import render
import requests
import datetime

def home(request):
    # Default city
    city = 'Kolkata'

    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']

    # OpenWeatherMap API endpoint with your API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=03ddfe8317ed1fd5f7f68a56fe0ffd3e'
    PARAMS = {'units': 'metric'}

    try:
        # Making the API request and fetching the response in JSON format
        data = requests.get(url, PARAMS).json()

        # Extracting relevant data from the API response
        description = data['weather'][0]['description'] 
        icon = data['weather'][0]['icon']  
        temp = data['main']['temp'] 

        day = datetime.datetime.today().strftime('%A, %d %B %Y')

        return render(request, 'index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
        })

    except (KeyError, IndexError, requests.exceptions.RequestException):
      
        return render(request, 'index.html', {
            'description': 'Data not available',
            'icon': '',
            'temp': 'N/A',
            'day': datetime.datetime.today().strftime('%A, %d %B %Y'),
            'city': city,
            'exception_occurred': True,
        })

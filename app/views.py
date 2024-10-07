from django.shortcuts import render
import requests
import datetime

def home(request):
    # Default city
    city = 'Kolkata'

    # If a city is provided in the POST request, use it
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']

    # OpenWeatherMap API endpoint with your API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=03ddfe8317ed1fd5f7f68a56fe0ffd3e'
    PARAMS = {'units': 'metric'}

    try:
        # Making the API request and fetching the response in JSON format
        data = requests.get(url, PARAMS).json()

        # Extracting relevant data from the API response
        description = data['weather'][0]['description']  # Weather description
        icon = data['weather'][0]['icon']  # Weather icon
        temp = data['main']['temp']  # Temperature in Celsius

        # Get today's date and format it nicely
        day = datetime.datetime.today().strftime('%A, %d %B %Y')

        # Render the 'index.html' with weather details
        return render(request, 'index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
        })

    except (KeyError, IndexError, requests.exceptions.RequestException):
        # Handle cases where the API returns an error or the city is invalid
        return render(request, 'index.html', {
            'description': 'Data not available',
            'icon': '',
            'temp': 'N/A',
            'day': datetime.datetime.today().strftime('%A, %d %B %Y'),
            'city': city,
            'exception_occurred': True,  # Use this flag in your template to show an error message
        })

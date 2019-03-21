from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.
def weather(request):
    if request.method == 'POST'and request.POST:
        city = request.POST['city']
        url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(city)
    else:
        url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
    try:
        json_data = requests.get(url).json()
        weather = json_data['results'][0]['weather_data']
        today_weather = weather[0]
        t_weather = weather[1]
        tt_weather = weather[2]
        ttt_weather =weather[3]
        city = json_data['results'][0]['currentCity']
    except Exception as e:
        return HttpResponse(e)
    else:
        context = {
            'today':today_weather,
            'city':city,
            'list':[t_weather,tt_weather,ttt_weather]
        }
        return render(request,'weather.html',context=context)

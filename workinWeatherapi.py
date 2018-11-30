import urllib2
import json

url = 'http://api.openweathermap.org/data/2.5/weather?q=Bangalore,india&appid=41598988b95c33b55a28559a0d4b4d4d'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)

#for item in data['weather']:
# print 'Weather forecast is :' + item['description'] 
print 'Weather forecast is :' + data['weather'][0]['description'] 	
print 'Minimum Temp is :' + str(data['main']['temp_min'])
print 'Maximum Temp is :' + str(data['main']['temp_max'])
print 'Current humidity is :' + str(data['main']['humidity'])
print 'Current windspeed is :' + str(data['wind']['speed'])


#OW_api_key = '41598988b95c33b55a28559a0d4b4d4d'


	
"""
{"coord":{"lon":77.6,"lat":12.98},
  "weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
  "base":"stations",
  "main":{"temp":301.15,"pressure":1017,"humidity":42,"temp_min":301.15,"temp_max":301.15},
  "visibility":10000,
  "wind":{"speed":3.6,"deg":70},
  "clouds":{"all":40},
  "dt":1543134600,
  "sys":{"type":1,"id":7823,"message":0.416,"country":"IN","sunrise":1543107176,"sunset":1543148412},
  "id":1277333,
  "name":"Bangalore",
  "cod":200
  }
"""

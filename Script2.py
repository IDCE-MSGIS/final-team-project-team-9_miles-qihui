import requests

zipcode = raw_input('Please input your US zipcode (Example: 01610, US:)')
#
# OPENWEATHERMAP_API_KEY = os.environ.get('dc97005f21d5744e0fdd1e405d09115b')

apikey = 'dc97005f21d5744e0fdd1e405d09115b'


url = 'https://api.openweathermap.org/data/2.5/weather/?q=%s&units=metric&appid=%s' % (zipcode, apikey)
#Example of complete URL https://api.openweathermap.org/data/2.5/weather/?q=01610&units=metric&appid=dc97005f21d5744e0fdd1e405d09115b
#Validated at https://codebeautify.org/jsonviewer
##params = {'q':city_name,'appid': OWMAP_APIKEY}

response = requests.get(url)
weatherdata = response.json()

## weatherdata now contains a list of nested dictionaries 
#JSON is a nested hierarchy file and in order to call the data you need to do a request.get and define your arguments

##coordinates = weatherdata['coord']

#Example of JSON API call: 
#{u'clouds': {u'all': 0}, u'name': u'Helsinki', u'visibility': 10000, u'sys': {u'country': u'FI', u'sunset': 1570376422, u'message': 0.0085, u'type': 1, u'id': 1332, u'sunrise':1570336616}, u'weather': [{u'main': u'Clear', u'id': 800, u'icon': u'01n', u'description': u'clear sky'}], u'coord': {u'lat': 60.25, u'lon': 24.87}, u'base': u'stations', u'timezone': 10800, u'dt': 1570311575, u'main': {u'pressure': 1020, u'temp_min': 0.56, u'temp_max': 2.78, u'temp': 1.92, u'humidity': 86},
#u'id': 658226, u'wind': {u'speed': 2.6, u'deg': 310}, u'cod': 200}

##print blank line
print "" 


#evaluate if the received "cod" key is not equal to "404", and if this evaluates to true, then the city has been located.
#If the "cod" key == "404" that means that the city is not found, and the else statement below is evaluated. 
if weatherdata["cod"] != "404": 
  
    # store the value of "main" in variable y 
  y = weatherdata["main"] 
    #store value of "coord"
   #add in statement regarding the weather	main "Rain"
  if 

    
  coordinates = weatherdata["coord"]  
  current_latitude = coordinates["lat"]
  current_latitude = coordinates["long"]
  
    # store the value of "temp" to the "temp" key of y 
  current_temperature_celsius = y["temp"] 
  #current_temperature_celsius integer conversion
  #converting the celcius temperature to farenheit
  temperature_farenheit = 9.0/5.0 * int(current_temperature_celsius) + 32
  current_temperature_farenheit = str(temperature_farenheit)

  
    # store the value corresponding to the "pressure" key of y 
  current_pressure = y["pressure"] 
  
    # store the value corresponding to the "humidity" key of y in "current_humidity"
  current_humidity = y["humidity"] 
  
    # store the corresponding values of "weather" key from weatherdata  in variable z 
  z = weatherdata["weather"] 
  
    # store the value corresponding  to the "description" key at the 0th index of z 
  weather_description = z[0]["description"] 
   #add in statement regarding the weather	main "Rain"
  if 
  
  
    # print following values 
  print(" The current weather conditions for your zipcode of " + zipcode + ":\n")
  print("_________________________________________\n")
  print(" Temperature (in Celsius) = " + str(current_temperature_celsius) + "\n Temperature (in Farenheit) = " + current_temperature_farenheit +  "\n Atmospheric Pressure (in hPa unit) = " + str(current_pressure) + "\n Humidity (in percent) = " + str(current_humidity) + "\n Current Weather Description = " + str(weather_description)) 

else: 
  print(" City Not Found ") 

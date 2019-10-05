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

## weatherdata now contains list of nested dictionaries 
print weatherdata
#JSON is a nested hierarchy file and in order to call the data you need to do a request.get and define your arguments

##latitude = weatherdata['coord']#['lat']

print "" 
##print latitude

if weatherdata["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
  y = weatherdata["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
  current_temperature = y["temp"] 

  
    # store the value corresponding 
    # to the "pressure" key of y 
  current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
  current_humidity = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
  z = weatherdata["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
  weather_description = z[0]["description"] 
  
    # print following values 
  print(" Temperature (in Celsius) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidity) + "\n description = " +str(weather_description)) 
else: 
  print(" City Not Found ") 

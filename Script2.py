import requests

cityname = raw_input('Please input your City (Example: Worcester:)')
#
# OPENWEATHERMAP_API_KEY = os.environ.get('dc97005f21d5744e0fdd1e405d09115b')

apikey = 'dc97005f21d5744e0fdd1e405d09115b'


url = 'https://api.openweathermap.org/data/2.5/weather/?q=%s&units=metric&appid=%s' % urlencode(cityname, apikey)
#Example of complete URL https://api.openweathermap.org/data/2.5/weather/?q=Chicago&units=metric&appid=dc97005f21d5744e0fdd1e405d09115b
#Validated at https://codebeautify.org/jsonviewer
##params = {'q':city_name,'appid': OWMAP_APIKEY}

response = requests.get(url)
weatherdata = response.json()
print weatherdata
#JSON is a nested hierarchy file and in order to call the data you need to do a request.get and define your arguments

results = weatherdata['coord']#['lat']

print results
###The data is called and returned 

# Place necessary comments and code here. 
import requests

# cityname = raw_input('Please input your City (Example: Worcester:)')

# OPENWEATHERMAP_API_KEY = os.environ.get('dc97005f21d5744e0fdd1e405d09115b')

OWMAP_APIKEY = 'dc97005f21d5744e0fdd1e405d09115b'

url = 'https://samples.openweathermap.org/data/2.5/weather'

params = {'q':'London,uk','appid': OWMAP_APIKEY}

response = requests.get(url=url, params=params)
business = response.json()
print business
#JSON is a nested hierarchy file and in order to call the data you need to do a request.get and define your arguments

rating = business['coord']['lat']

print rating
###'''page = requests.get(url)
##soup = BeautifulSoup(page.text,"html.parser")
###city_results = []

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
# all_results = soup.findall("forecast-list")
# all_results = all_results.text
# print all_results
###for div in soup.findAll("div",{"class":"container"}):
   ###print div.text

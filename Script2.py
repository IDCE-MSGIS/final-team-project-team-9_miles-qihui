# Place necessary comments and code here. 
##The program itself asks a user for a city input and the input is then added as the ending argument for the URL https://openweathermap.org/find?q=
##The program then returns the first 5 results for a city and asks the user to confirm which city is theirs through the command
##"Please confirm which city is the correct one by entering its corresponding number "first", "second", "third", "fourth", "fifth"
##The user input is then evaluated and compared to the stored values scraped and the ostensive city result is produced with the corresponding weather data


##First part of code which retrieves asks the user for a city input 
import requests
from bs4 import BeautifulSoup
#import pgeocode

cityname = raw_input('Please input your City (Example: Worcester:)')

city_results = []

def deadWeather(cityname):
  url = 'https://openweathermap.org/find?q='+cityname
  page = requests.get(url)
  soup = BeautifulSoup(page.text,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
  all_results = soup.findAll("b")
  for cities in all_results:
    cities = all_results.get_text()
    city_results.append(cities)

print(deadWeather(cityname))

#g = geocoder.geonames(zippy)
#g.latlng
##for result in g:
  ##print(result.address, result.latlng)

# List to store response

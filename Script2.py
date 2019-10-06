# completed Script 2 for Python Final Project.  The script takes a user input of a zipcode and calls data from the OpenWeatherMap API.  
# The data is returned in a json file which is then passed and processed into various functions to be returned to the user.  
# The user is presented with a menu of options 1-6 (1-5 for weather data, and 6 to quit) for the data which they would like to access for the entered zipcode. 
# The data is returned to the user and they have the option of finding more data from the area or quitting the program. 

#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import time
import sys

#Created a class weather_function to house the functions we will utilize in our menu for the user to specify their data
class weather_function():
    # define a function to get the API response
    def get_weatherdata(self):
      # ask user to input a US zipcode 
      zipcode = raw_input('Please input your US zipcode (Example: 01610, US:)')
      apikey = 'dc97005f21d5744e0fdd1e405d09115b'
      url = 'https://api.openweathermap.org/data/2.5/weather/?q=%s&units=metric&appid=%s' % (zipcode, apikey)
      # units=metric is specified to return the temperature in Celsius.  The default output in the JSON file is in Kelvin degrees. 
      #Example of complete URL https://api.openweathermap.org/data/2.5/weather/?q=01610&units=metric&appid=dc97005f21d5744e0fdd1e405d09115b
      #Validated at https://codebeautify.org/jsonviewer
      response = requests.get(url)
      weatherdata = response.json()
      ## weatherdata now contains list of nested dictionaries 
      #JSON is a nested hierarchy file and in order to return the json data from "response" which is then stored in weatherdata to the user, you need to identify the keys and values in teh json file. 
      #Example of the result of a JSON API call for 01610 without specifying the county code of 'us': 
      #{u'clouds': {u'all': 0}, u'name': u'Helsinki', u'visibility': 10000, u'sys': {u'country': u'FI', u'sunset': 1570376422, u'message': 0.0085, u'type': 1, u'id': 1332, u'sunrise':1570336616}, u'weather': [{u'main': u'Clear', u'id': 800, u'icon': u'01n', u'description': u'clear sky'}], u'coord': {u'lat': 60.25, u'lon': 24.87}, u'base': u'stations', u'timezone': 10800, u'dt': 1570311575, u'main': {u'pressure': 1020, u'temp_min': 0.56, u'temp_max': 2.78, u'temp': 1.92, u'humidity': 86},
      #u'id': 658226, u'wind': {u'speed': 2.6, u'deg': 310}, u'cod': 200}
      return weatherdata
    
    # a function to print current humidity using the data stored in weatherdata and object passed as self
    def current_humidity(self,weatherdata):
        print('humidity (in percentage): '+str(weatherdata["main"]["humidity"]) )
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown!\n")
        
    # a function to print current pressure using the data stored in weatherdata and object passed as self
    def current_pressure(self,weatherdata):
        print('atmospheric pressure (in hPa unit):'+str(weatherdata["main"]["pressure"]))
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown! \n")

    # a function to print current Temperature (in Celsius) using the data stored in weatherdata and object passed as self
    def current_temperature_C(self,weatherdata):
        print('Temperature (in Celsius):'+str(weatherdata["main"]["temp"] ) )
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown!\n")

    # a function to print current Temperature (in Fahrenheit) using the data stored in weatherdata and object passed as self
    def current_temperature_F(self,weatherdata):
        t_c=weatherdata["main"]["temp"]
        t_f=t_c*1.6+32
        print('Temperature (in Fahrenheit):'+str(t_f ) )
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown!\n")

    # a function to print weather description using data stored as weatherdata and object passed as self
    def weather_description(self,weatherdata):
        print('weather description:'+str(weatherdata["weather"][0]["description"]))
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown!\n")
        
#create the menu 
class Menu():
   #_init_() is the special Python name for a method that initializes an individual object from its class definition. 
    #The self argument specifies that it refers to the individual object itself.
    def __init__(self):
        #Give an instance of the function
        self.weather_function = weather_function()
        self.choices = {
            "1": self.weather_function.current_humidity,
            "2": self.weather_function.current_pressure,
            "3": self.weather_function.current_temperature_C,
            "4": self.weather_function.current_temperature_F,
            "5": self.weather_function.weather_description,
            "6": self.quit
        }
    # display the menu to the user
    def display_menu(self):
        print("""
Operation Menu:
1. Current Humidity
2. Current Pressure
3. Current Temperature in Celsius
4. Current Temperature in Fahrenheit
5. Weather Description
6. Quit
""")

    def run(self):
        print('Welcome!\n')
        weatherdata=self.weather_function.get_weatherdata()
        count=0
        #Exception handling
        while True:
            
            #Evaluate if the received "cod" key is equal to "200" which means that the zipcode was valid. 
            #If it is not, then the user is informed to enter a valid zipcode.
            #The count is then increased by 1 and the if statement is evaluated to allow the continued running of the script 
            if weatherdata['cod'] != 200:
              print("Please input a valid zipcode!");
              count=count+1
              if count>0:
                weatherdata=self.weather_function.get_weatherdata()
              continue
            
            #Evaluate if the received "cod" key is not equal to "404", and if this evaluates to true, then the city has been located.
            #The count is then increased by 1 and the if statement is evaluated to allow the continued running of the script 
            elif weatherdata["cod"] ==404:
              print("City not found!");
              count=count+1
              if count>0:
                weatherdata=self.weather_function.get_weatherdata()
              continue 

            self.display_menu()
            #Get user input of menu choice 
            #Tests whether the user input was a valid option and continues the evaluation of their input.
            #If not a valid option, the user is asked to input a valid option 
            try:
                choice = input("Enter an option: ")
            except Exception as e:
                print("Please input a valid option!");
                continue
            #Associate the user input with function
            choice = str(choice).strip()
            action = self.choices.get(choice)
            #Determines if the user's choice(input) was one of the options 1-5. 
            #If the option was 6, then then the quit function (defined below) stored in object passed as self is run. 
            if choice in {'1','2','3','4','5'}:
                action(weatherdata)
            elif choice=='6':
                action()    
            else:
                print("{0} is not a valid choice".format(choice))
    #Define a function to quit the script with user input of "0" for when the user decides to quit examining the weather. 
    def quit(self):
        print("\nThank you for using this script!\n")
        sys.exit(0)

#If statement to start the program
if __name__ == '__main__':
    Menu().run()

#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import time
import sys

class weather_function():
    # define a function to get the API response
    def get_weatherdata(self):
      # ask user to input a zipcode 
      zipcode = raw_input('Please input your US zipcode (Example: 01610, US:)')
      apikey = 'dc97005f21d5744e0fdd1e405d09115b'
      url = 'https://api.openweathermap.org/data/2.5/weather/?q=%s&units=metric&appid=%s' % (zipcode, apikey)
      #Example of complete URL https://api.openweathermap.org/data/2.5/weather/?q=01610&units=metric&appid=dc97005f21d5744e0fdd1e405d09115b
      #Validated at https://codebeautify.org/jsonviewer
      response = requests.get(url)
      weatherdata = response.json()
      ## weatherdata now contains list of nested dictionaries 
      #JSON is a nested hierarchy file and in order to call the data you need to do a request.get and define your arguments
      return weatherdata
    # a function to print current humidity
    def current_humidity(self,weatherdata):
        print('humidity (in percentage): '+str(weatherdata["main"]["humidity"]) )
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown!\n")
        
    # a function to print current pressure
    def current_pressure(self,weatherdata):
        print('atmospheric pressure (in hPa unit):'+str(weatherdata["main"]["pressure"]))
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown! \n")

    # a function to print current Temperature (in Celsius)
    def current_temperature_C(self,weatherdata):
        print('Temperature (in Celsius):'+str(weatherdata["main"]["temp"] ) )
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown!\n")

    # a function to print current Temperature (in Fahrenheit)
    def current_temperature_F(self,weatherdata):
        t_c=weatherdata["main"]["temp"]
        t_f=t_c*1.6+32
        print('Temperature (in Fahrenheit):'+str(t_f ) )
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown!\n")

    # a function to print weather description
    def weather_description(self,weatherdata):
        print('weather description:'+str(weatherdata["weather"][0]["description"]))
        #suspends execution for the given number of seconds
        time.sleep(1)
        print("\nAll the imformation has shown!\n")
        
#create the menu 
class Menu():
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
            
            if weatherdata['cod'] != 200:
              print("Please input a valid zipcode!");
              count=count+1
              if count>0:
                weatherdata=self.weather_function.get_weatherdata()
              continue
            
            elif weatherdata["cod"] ==404:
              print("City not found!");
              count=count+1
              if count>0:
                weatherdata=self.weather_function.get_weatherdata()
              continue 

            self.display_menu()
            # get user input of menu choice 
            try:
                choice = input("Enter an option: ")
            except Exception as e:
                print("Please input a valid option!");
                continue
            #associate the user input with function
            choice = str(choice).strip()
            action = self.choices.get(choice)
            if choice in {'1','2','3','4','5'}:
                action(weatherdata)
            elif choice=='6':
                action()    
            else:
                print("{0} is not a valid choice".format(choice))
    #define a function to quit the script
    def quit(self):
        print("\nThank you for using this script!\n")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()

## Final Project: Script 1
### Web-scraping Weather Forecast Information with Python

#### 1.Goal of the script: 

We scraped the 5-day weather forecast from the National Weather Service website and extracted information from multiple elements listed under the same class name using the BeautifulSoup library. In order to make the crawling results display more readily readable/intuited, we added spaces and commas in the output to breakup incorrect compounding of words and converted all the output to uppercase. 

#### 2.Method:
We found 2 ways to achieve the goals:
The first one was to observe the characteristics of crawling information, and using Python string replace() method to add spaces in front of the uppercase letter, add comma in front of the ‘High’ and ‘Low’, and remove extra spaces. In this way, the extracted information was still stored in the list and we directly did the modifications in the list.
The second one was to find the positions of the two adjacent letters that are one uppercase and another lowercase, then add space in front of the uppercase letter. Different from the last way, in this way, we created a new string to store the modified information, and the information in the list was unchanged. 

#### 3.Conclusion:
In the future, we have great possibilities to use similar scripts to crawl information from the website. However, compared to the first way described in the front, the second way would be more extensive, and the applicability in different cases would be greater.


## Final Project: Script 2
### Current Weather Query Python Script Based on Open Weather Map API


#### 1. Initial Goal of the script:


The initial goal of our script was to give the user an accurate description of the weather conditions based on their input -- a US zipcode and return the forecast for the day in an intuitive GUI format(still in developing) using and the OpenWeatherMap Current Weather data API.

The “forecast” is defined as the following:
--current humidity;
--current pressure;
--weather description; and
--Temperature (Celsius and Farenheit).


#### 2.Method:
We went about creating this script by first looking for similar projects which have attempted this goal.  We found a GUI toolkit called PyQt which allows for the creation of GUIs using python code. Our plan was to export this created GUI as a self-contained widget so that anyone could download it and use it without having to install packages. However, we had some difficulties like problems of PyQt's and Systerm enviromental.

Instead of the GUI, We decided to create a "menu" from which the user can specify the data they would like to see, making an interface for users to specify their desired data.  We went about creating the proper URL for the API call in accordance with API documentation available on Open Weather Map (https://openweathermap.org/current). Once we were able to successfully create the URL, we tested the resulting JSON file using https://codebeautify.org/jsonviewer and evaluated the nested dictionaries for the keys and values (weather data) we desired. The new script takes a user input of a zipcode and calls data from the OpenWeatherMap API. The data is returned in a json file which is then passed and processed into various functions to be returned to the user. The user is presented with a menu of options 1-6 (1-5 for weather data, and 6 to quit) for the data which they would like to access for the entered zipcode. The data is returned to the user and they have the option of finding more data from the area or quitting the program.

#### 3.Conclusion:
In the process of creating something which worked we sacrificed the incorporation of the GUI and clothing recommendations. In the future, we would like to be able to provide a self contained widget to the user for them to utilize without having to run the code through a compiler.  In addition we would like to make it so the user has the option of opting out of the initial selected city and input new cities for them to examine. In the meantime though, we learned valuable lessons about time constraints, the process of API calls, JSON files, creating classes/objects in python, and about the value of adapting to unforeseen externalities such as data being locked behind paywalls and programming language limitations in implementations of newer libraries.


#### 4.Resources:
For information on creating a GUI using PyQT5
https://www.learnpyqt.com/apps/create-desktop-weather-app/


For understanding the Requests library
https://realpython.com/python-requests/#the-response


For the python code for the Farenheit to Celcius conversion
https://www.pythonforbeginners.com/code-snippets-source-code/python-code-celsius-and-fahrenheit-converter


For the API documentation for OpenWeatherMap
https://openweathermap.org/current

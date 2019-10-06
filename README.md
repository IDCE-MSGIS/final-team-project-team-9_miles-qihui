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
### Current Weather Data for User defined zipcode using Open Weather Map


#### 1. Initial Goal of the script:


In our script we wanted to take webscraping lab (Lab 5) and modified it so that the weatherdata would be called from a resource using an API key instead of by means of a web scraper-- which can be blocked by certain sites by disallowing their content from being scraped using dynamic content. The initial goal of our script was to give the user an accurate description of the weather conditions based on their input -- a US zipcode and return the forecast for the day in an intuitive GUI format using the PyQT binding and the OpenWeatherMap Current Weather data API.


The “forecast” is defined as the following:
--Current description of the weather outside;
--Wind Speed;
--Humidity; and
--Temperature (Celsius and Farenheit).


Following the call and return of this data the script would give a recommendation for certain clothing items (E.g. umbrella for rain, boots & jacket for snow; windproof clothing for windy days.


#### 2.Method:
We went about creating this script by first looking for similar projects which have attempted this goal.  We found in our research a C++/Python binding called PyQt which allows for the creation of GUIs using python code. We then set about examining how the binding works and what elements are involved in displaying the data in a GUI.  We found the resource Qt Creator which allows a user to build the GUI using a GUi and then specify how the elements in the GUI (i.e. the buttons and the output display) work by writing in supplementary code in combination with the PyQt generated code for the labels and display elements in the GUI--essentially post-hoc coding. Our plan was to then export this created GUI as a self-contained widget so that anyone could download it and use it without having to install packages. However, we quickly found the interface was prohibitive in creating the GUI without more knowledge of C++ and that the most recent PyQt packages do not function with Python 2.  In addition, the free version of the API we were using from https://openweathermap.org/current does not allow the user to call the forecast data without having a premium subscription and would only allow us to call the weather data instead.

Instead of the GUI, we then concentrated our efforts on understanding how to incorporate an API call into our code and extracting data from the resultant JSON file created as a result of the API call. We wanted to still produce the outputs from our proposal for the user and make an interface for users to specify their desired data. We decided to create a "menu" from which the user can specify the data they would like to see.  We went about creating the proper URL for the API call in accordance with API documentation available on Open Weather Map (https://openweathermap.org/current). Once we were able to successfully create the URL, we tested the resulting JSON file using https://codebeautify.org/jsonviewer and evaluated the nested dictionaries for the keys and values (weather data) we desired. We then made a first draft of the code which evaluated the input of the user --the zipcode and country code for the US-- and returned to them the desired outputs listed previously. Once we had a reliable version of the code that functioned when we ran it, we went about improving it by learning how to utilize classes, the self argument, and inheritance in order to simplify the code from innumerable if statements and loops. After modifying the script with our new-found knowledge we were able to run our script with repeated success. In short, the new script takes a user input of a zipcode and calls data from the OpenWeatherMap API. The data is returned in a json file which is then passed and processed into various functions to be returned to the user. The user is presented with a menu of options 1-6 (1-5 for weather data, and 6 to quit) for the data which they would like to access for the entered zipcode. The data is returned to the user and they have the option of finding more data from the area or quitting the program.

#### 3.Conclusion:
In the process of creating something which worked we sacrificed the incorporation of the GUI and clothing recommendations. In the future, we would like to be able to provide a self contained widget to the user for them to utilize without having to run the code through a compiler.  In addition we would like to make it so the user has the option of opting out of the initial selected city and input new cities for them to examine. In the meantime though, we learned valuable lessons about time constraints, the process of API calls, JSON files, creating classes/objects in python, and about the value of adapting to unforeseen externalities such as data being locked behind paywalls and programming language limitations in implementations of newer libraries (Python 2 I'm looking at you).


#### 4.Resources:
For information on creating a GUI using PyQT5
https://www.learnpyqt.com/apps/create-desktop-weather-app/


For understanding the Requests library
https://realpython.com/python-requests/#the-response


For the python code for the Farenheit to Celcius conversion
https://www.pythonforbeginners.com/code-snippets-source-code/python-code-celsius-and-fahrenheit-converter


For the API documentation for OpenWeatherMap
https://openweathermap.org/current

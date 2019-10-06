## Final Project: Documentation of Script 1 and Script 2
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
### Your Chosen Assignment

#### 1. Initial Goal of the script: 

In our script we wanted to take the previously completed webscraping lab and modify it so that the data would be called from a resource using an API key instead of by means of a web scraper-- which can be blocked by certain sites by disallowing their content from being scraped using dynamic content. The initial goal of our script was to give the user an accurate description of the weather conditions based on their input -- a US zipcode and return the fortecast for the day in an intuitive GUI format using the PyQT binding and the OpenWeatherMap Current Weather data API.

The “forecast” is defined as the following:
--Current description of the weather outside;
--Wind Speed;
--Humidity; and
--Temperature.

Following the call and return of this data the script would give a recommendation for certain clothing items (E.g. umbrella for rain, boots & jacket for snow; windproof clothing for windy days.  Return temperature  based on preference for Celsius or Fahrenheit.


#### 2.Method:
We went about creating this script by first looking for similar projects which have attempted this goal.  We found in our research a C++/Python binding called PyQt which allows for the creation of GUIs using python code. We then set about examining how the binding works and what elements are involved in displaying the data in a GUI.  We found the resource Qt Creator which allows a user to build the GUI using a GUi and then specify how the elements in the GUI (i.e. the buttons and the output display) work by writing in supplementary code in combination with the PyQt generated code for the labels and display elements in the GUI--essentially post-hoc coding. Our plan was to then export this created GUI as a self-contained widget so that anyone could download it and use it without having to install packages. However, we quickly found the interface was prohibitive in creating the GUI without more knowledge of C++ and that the most recent PyQt packages do not funciton with Python 2.  In addition, the free version of the API we were using from https://openweathermap.org/current does not allow the user to call the forecast data without having a premium subscription and would only allow us to call the weather data instead. 

Instead of the GUI, we then  oncentrated our efforsts on understandinghow to incorporate an API call into our code and extracting data from the resultant JSON file created as a result of the API call. We wanted to still produce options for the user 

#### 3.Conclusion:
In the future, we have great possibilities to use similar scripts to crawl information from the website. However, compared to the first way described in the front, the second way would be more extensive, and the applicability in different cases would be greater.


The script which we pulled from 


#### 4.Resources:
For information on creating a GUI using PyQT5
https://www.learnpyqt.com/apps/create-desktop-weather-app/

For understanding the Requests library
https://realpython.com/python-requests/#the-response

For the python code for the Farenheit to Celcius conversion
https://www.pythonforbeginners.com/code-snippets-source-code/python-code-celsius-and-fahrenheit-converter 

For the API documentation for OpenWeatherMap
https://openweathermap.org/current

For the String Encoding:
https://www.learnpython.org/en/String_Formatting

For evaluating the JSON
https://codebeautify.org/jsonviewer
For Learning about Classes 
Introducing Python - Modern Computing in Simple Packages - Bill Lubanovic OReilly Publishing





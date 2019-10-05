## Final Project: Documentation of Script 1
### Web-scraping Weather Forecast Information with Python

#### 1.Goal of the script: 

We scraped the 5-day weather forecast from the National Weather Service website and extracted information from multiple elements listed under the same class name using the BeautifulSoup library. In order to make the crawling results displayed more readably and neatly, we added spaces in the proper place of the output and convert the it to uppercase. 

#### 2.Method:
We found 2 ways to achieve the goals:
The first one was to observe the characteristics of crawling information, and using Python string replace() method to add spaces in front of the uppercase letter, add comma in front of the ‘High’ and ‘Low’, and remove extra spaces. In this way, the extracted information was still stored in the list and we directly did the modifications in the list.
The second one was to find the positions of the two adjacent letters that are one uppercase and another lowercase, then add space in front of the uppercase letter. Different from the last way, in this way, we created a new string to store the modified information, and the information in the list was unchanged. 

#### 3.Conclusion:
In the future, we have great possibilities to use similar scripts to crawl information from the website. However, compared to the first way described in the front, the second way would be more extensive, and the applicability in different cases would be greater.


## Final Project: Script 2
### Your Chosen Assignment
For this script, you will complete the assignment that you have proposed, which involves modifying a previous exercise. Remember to update the Script2.py file to include comments and documentation in your script to tell me what it’s doing!




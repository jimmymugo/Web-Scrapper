import pandas as pd
import requests
from bs4 import BeautifulSoup


page =requests.get('https://forecast.weather.gov/MapClick.php?lat=39.3237&lon=-111.6782')

soup =BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all(''))

week =soup.find(id="seven-day-forecast-body")

#print(week)
items = week.find_all(class_='tombstone-container')
#print(items)

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_="temp").get_text())

period_names =[item.find(class_='period-name').get_text() for item in items]
short_descriptions =[item.find(class_='short-desc').get_text() for item in items]
temperatures=[item.find(class_="temp").get_text() for item in items]

#print(period_names)
#print(short_descriptions)
#print(temperatures)


weather_stuff = pd.DataFrame(
    {'period_name':period_names,
    'short_descriptions':short_descriptions,
    'temperatures':temperatures,
    }

)
print(weather_stuff)

weather_stuff.to_csv('Weather.csv')
# Exploring page structure with Chrome DevTools

import requests
from bs4 import BeautifulSoup

print("Download the web page containing the forecast.")
print("Create a BeautifulSoup class to parse the page.")
print("Find the div with id seven-day-forecast, and assign to seven_day")
print("Inside seven_day, find each individual forecast item.")
print("Extract and print the first forecast item.")
print("-----------------------------------------------------------------")

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

# Extracting information from the page

print("There are 4 pieces of information we can extract")
print("The name of the forecast item — in this case, Tonight.")
print("The description of the conditions — this is stored in the title property of img.")
print("A short description of the conditions — in this case, Mostly Clear.")
print("The temperature low — in this case, 49 degrees.")
print("-------------------------------------------------")

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

print("Now, we can extract the title attribute from the img tag")
img = tonight.find("img")
desc = img['title']
print(desc)

#Extracting all the information from the page

print("Extracting al the information from the page")
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

print(".")
print("We can apply the same technique to get the other 3 fields:")
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)

#Combining our data into a Pandas Dataframe

import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
print(weather)

print("We can use a Reg Ex and the Series.str.extract to pull out")
print("the numeric temperature values:")
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)

print("We could then find the mean of all the high and low temperatures:")
print( weather["temp_num"].mean() )

print("We could also only select the rows that happen at night")
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)

print( weather[is_night] )




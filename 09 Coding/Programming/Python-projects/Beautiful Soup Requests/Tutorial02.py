# Searching for tags by class and id

import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

print("We can use the find_all method to search for items by class or by id")
print( soup.find_all('p', class_='outer-text') )

print("We'll look for any tag that has the class outer-text")
print( soup.find_all(class_="outer-text") )

print("We can also search for elements by id:")
print( soup.find_all(id="first"))

# Using CSS Selectors
print("Using CSS selectors")
print( soup.select("div p"))



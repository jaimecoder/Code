#Scrape de títulos de andaluciaemprende.es

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.andaluciaemprende.es/noticias/", verify=False)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')

print("Explorando el tag h1")
print(soup.find_all('h1'))

print("Looping find_all to extract text (from first h1 instance) ")
print ( soup.find_all('h1')[0].get_text() )

print("find_all to search for items by class or by id")
print( soup.find_all('h1', class_='entry-title') )

print("Extracting information from the page")
findbyid = soup.find(class_="page-items") 
title_tags = findbyid.select(".entry-title")
titles = [tt.get_text() for tt in title_tags]
print(titles)

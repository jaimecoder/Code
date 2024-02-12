#First part

import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print(page.status_code)
print(page.content)

#Parsing a page with BeautifulSoup

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

print("Using the children property of soup")
print(list(soup.children))

print("What the type of each element in the list is:")
print( [type(item) for item in list(soup.children)] )

print("We select the html tag and its children")
html = list(soup.children)[2]
print( list(html.children) )

print("We want to extract the text inside the p tag.")
body = list(html.children)[3]
print ( list(body.children) )

print("We can now isolate the p tag:")
p = list(body.children)[1]

print("Once we've isolated the tag, we can use the get_text method to extract")
print("all of the text inside the tag:")
print( p.get_text() )

# Finding all instances of a tag at once

print("------------------------------------")
print("Finding all instances of a tag at once")
soup = BeautifulSoup(page.content, 'html.parser')
print( soup.find_all('p') )

print("List indexing to extract text")
print( soup.find_all('p')[0].get_text() )

print("To find only the first instance of a tag")
print( soup.find('p'))







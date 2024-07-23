
'''
Created on Aug 21, 2018

Course work:

@author:

Source:

'''

from bs4 import BeautifulSoup
import requests
import os, os.path


url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup)

# listings = []
for row in soup.select("section div ol li"):
    # print(row)

    link = row.select("a")[1]
    # print(link)

    link_text = link.get_text()
    link_href = link['href']
    print(f'Text: {link_text}, Href: {link_href}')

for row in soup.select("section div ol li div "):

    price= row.select("p ")

    link1_text=price.get_text()
    #link1_href = img['href']
    print(f'text: {price}')
      
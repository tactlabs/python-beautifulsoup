
'''
Created on Aug 21, 2018

Course work:

@author:

Source:
    https://books.toscrape.com/
'''

from bs4 import BeautifulSoup
import requests
import os, os.path
import json


url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup)

def get_book_details():

    book_list = []
    for row in soup.select("section div ol li"):
        # print(row)

        link = row.select("a")[1]
        # print(link)

        link_text = link.get_text()
        link_href = link['href']
        # print(f'Text: {link_text}, Href: {link_href}')

        book_list.append({
            'title' : link_text,
            'link' : link_href
        })

    return book_list

def get_price():

    price_list = []
    for row in soup.select("section div ol li article div p.price_color"):
        price  = row.get_text()
        # print(f'price: {price}')

        price_list.append(price)

    return price_list

def convert_to_symbol(price):

    # decoded_string = price.encode().decode('unicode_escape')
    decoded_string = price.encode('latin1').decode('utf-8')
    cleaned_price = decoded_string.replace("Â", "")

    return cleaned_price

def startpy():

    # print("Tact101")

    book_list = get_book_details()
    price_list = get_price()

    # print(book_list)
    # print(price_list)

    final_list = []
    for idx, book in enumerate(book_list):
        final_list.append({
            'id' : 12000 + idx,
            'title' : book['title'],
            'link' : book['link'],
            'price' : convert_to_symbol(price_list[idx])
        })

    # print(final_list)

    print(json.dumps(final_list, indent=4))


if __name__ == '__main__':
    startpy()
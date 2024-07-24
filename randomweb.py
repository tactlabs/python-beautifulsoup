from bs4 import BeautifulSoup
import requests
import os, os.path
import json


url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup)

def get_book_details():

    book_list = []
    for row in soup.select("div.product_main h1"):
        # print(row)

        link = row.select("a")[1]
        # print(link)

        link_text = link.get_text()
        # link_href = link['href']
        # print(f'Text: {link_text}, Href: {link_href}')

        book_list.append({
            'title' : link_text
            # 'link' : link_href
        })

    return book_list

def get_title():

    title_list = []
    for row in soup.select("div.product_main h1"):
        title  = row.get_text()
        # print(f'price: {price}')

        title_list.append(title)

    return title_list

def get_price():
    price_list = []
    for row in soup.select("div.product_main p.price_color"):
        price = row.get_text()

        price_list.append(price)
    return price_list

def get_stock():
    stock_list = []
    for row in soup.select("div.product_main p.instock.availability"):
        stock=row.get_text()
        stock_list.append(stock)
    return stock_list


def get_star():
    star_list = []
    for row in soup.select("div.product_main p.star-rating.Three"):
        star = row.get_text()
        star_list.append(star)
    return star_list


def get_description():
    description_list=[]
    for row in soup.select("div.product_main div"):
        description = row.get_text()
        description_list.append(description)
    return description_list


def convert_to_symbol(price):

    # decoded_string = price.encode().decode('unicode_escape')
    decoded_string = price.encode('latin1').decode('utf-8')
    cleaned_price = decoded_string.replace("Â", "")

    return cleaned_price

def startpy():

    # print("Tact101")

    # book_list = get_book_details()
    # print(f'book_list:{book_list}')
    
    title = get_title()
    print(f'title:{title}')

    price_list = get_price()
    print(f'price_list:{price_list}')


    description_list=get_description()
    print(f'description_list:{description_list}')

    stock_list = get_stock()
    print(f'stock_list:{stock_list}')

    star_list = get_star()
    print(f'star_list:{star_list}')
    # final_list = []
    # for idx, book in enumerate(book_list):
    #     final_list.append({
    #         'id' : 12000 + idx,
    #         'title' : book['title'],
    #         'link' : book['link'],
    #         'price' : convert_to_symbol(price_list[idx])
        # })

    # print(final_list)

    # print(json.dumps(final_list, indent=4))


if __name__ == '__main__':
    startpy()
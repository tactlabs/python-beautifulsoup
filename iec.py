#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error
#from sympy.polys.polytools import quo

'''
Created on Aug 21, 2018

Course work:

@author:

Source:
    Indian Election Commisison


'''

from bs4 import BeautifulSoup
import requests
import os, os.path

def get_details():

    url = "https://results.eci.gov.in/PcResultGenJune2024/partywiseleadresultState-369.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # listings = []
    # for rows in soup.find_all("table-bordered tr"):
    #     if ("oddrow" in rows["class"]) or ("evenrow" in rows["class"]):

    #         name = rows.find("div", class_="name").a.get_text()

    #         hometown = rows.find_all("td")[1].get_text()

    #         school = hometown[hometown.find(",")+4:]

    #         city = hometown[:hometown.find(",")+4]

    #         position = rows.find_all("td")[2].get_text()

    #         grade = rows.find_all("td")[4].get_text()

    #         listings.append([name, school, city, position, grade])

    # print(listings)

    table = soup.find('table', class_='table-bordered')
    rows = table.find_all('tr')

    for row in rows:
        # print(row)  # This will print each 'tr' element

        columns = row.find_all('td')
        for column in columns:
            # print(column)  # This prints the HTML element
            print(column.text)  # This prints the text within the column

        print(f'-'*100)


def startpy():

    # print("Tact101")

    get_details()


if __name__ == '__main__':
    startpy()
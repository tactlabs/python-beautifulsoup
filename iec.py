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

    table = soup.find('table', class_='table-bordered')
    rows = table.find_all('tr')

    result_list = []
    for idx, row in enumerate(rows):
        # print(row)  # This will print each 'tr' element

        columns = row.find_all('td')

        cdict = {}
        for idx, column in enumerate(columns):
            # print(column)  # This prints the HTML element
            # print(column.text)  # This prints the text within the column

            if(idx == 0):
                cdict['id'] = column.text
            elif(idx == 1):
                cdict['constituency'] = column.text
            elif(idx == 2):
                cdict['leading'] = column.text
            elif(idx == 3):
                cdict['votes'] = int(column.text)
            elif(idx == 4):
                cdict['margin'] = int(column.text)

        # print(f'cdict: {cdict}')
        # print(f'-'*100)

        result_list.append(cdict)

    return result_list

def startpy():

    # print("Tact101")

    get_details()


if __name__ == '__main__':
    startpy()
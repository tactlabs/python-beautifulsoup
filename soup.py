
'''
Created on Aug 21, 2018

Course work:

@author:

Source:

'''

from bs4 import BeautifulSoup
import requests
import os, os.path


url = "http://www.espn.com/college-sports/football/recruiting/databaseresults/_/sportid/24/class/2006/sort/school/starsfilter/GT/ratingfilter/GT/statuscommit/Commitments/statusuncommit/Uncommited"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

listings = []
for rows in soup.find_all("tr"):
    if ("oddrow" in rows["class"]) or ("evenrow" in rows["class"]):

        name = rows.find("div", class_="name").a.get_text()

        hometown = rows.find_all("td")[1].get_text()

        school = hometown[hometown.find(",")+4:]

        city = hometown[:hometown.find(",")+4]

        position = rows.find_all("td")[2].get_text()

        grade = rows.find_all("td")[4].get_text()

        listings.append([name, school, city, position, grade])

print(listings)
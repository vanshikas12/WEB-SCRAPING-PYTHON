#importing libraries

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

#creating empty lists
product = []
price = []
rating = []
description = []

page = range(1, 10) #range of pages

for page_no in page:

    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=" + str(
        page_no)
    response = requests.get(url)
    time.sleep(2)

    r = response.content
    soup = BeautifulSoup(r, "html.parser")
    # print(soup.prettify())

    for content in soup.find_all("div", attrs={"class": "yKfJKb row"}):

        # Getting the product name.
        pr = content.find("div", attrs={"class": "KzDlHZ"}).text
        product.append(pr)

        # Getting the price.
        pri = content.find("div", attrs={"class": "Nx9bqj _4b5DiR"}).text
        price.append(pri)
        
        # Getting product description.
        desc = content.find("div", attrs={"class": "_6NESgJ"}).text
        description.append(desc)

        # Getting the Ratings(using try and except block because some ratings are missing).
        try:
            rate = content.find("div", attrs={"class": "XQDdHH"}).text
            rating.append(rate)
        except Exception as e:
            rate = None
            rating.append(rate)

# Creating a dataframe 
df = pd.DataFrame({'MODEL': product, 'PRICE': price, 'RATING': rating, 'DESCRIPTION': description})
print(df)

#Storing the data to a csv file
df.to_csv('C:/Users/kinsh/Desktop/tryytry/worked2.csv')
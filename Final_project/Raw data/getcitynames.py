import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

def scroll_down(driver):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height


# df = pd.DataFrame(columns=['Name', 'City', 'Location', 'Price', 'Property Type', ])
# df = pd.DataFrame
links=[]
# print(df)
url = 'https://www.agoda.com/en-gb/search?city='

# city_code -> name = map()
city_code_map = dict()
city_names = list()
city_codes = list()
added_cities = list()
for i in range(11000,11500):
    driver = webdriver.Safari()

    urlnew = url+str(i)+'&hotelAccom=34'
    driver.get(urlnew)
    # driver.get('https://www.agoda.com/en-gb/search?city=11304&hotelAccom=34')
    
    # # driver.fullscreen_window()
    time.sleep(1)
    # scroll_down(driver)
    # time.sleep(3)

    soup = BeautifulSoup(driver.page_source , 'html.parser')

    res = soup.find('div', attrs = {'class':'SearchBoxTextDescription__title'})

    print(i  , res.get_text())
    if(res.get_text() != '' and (res.get_text() not in added_cities)):
        city_codes.append(i)
        city_names.append(res.get_text())
        added_cities.append(res.get_text())
    # city_code_map[i] = table.get_text()
    driver.close()

df = pd.DataFrame({'city_code' : city_codes, 'city_name':city_names})
print(df)
# print(df['city_code'].tolist())
df.to_csv('file.csv')




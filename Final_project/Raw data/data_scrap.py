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
        time.sleep(3)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height


# df = pd.DataFrame(columns=['Name', 'City', 'Location', 'Price', 'Property Type', ])
df = pd.DataFrame(columns=['links'])

links=[]
# print(df)
driver = webdriver.Safari()
# driver.get('https://www.agoda.com/en-gb/search?city=11304&checkIn=2023-03-18&los=1&rooms=1&adults=2&children=0&locale=en-gb&ckuid=f17c2e5d-d451-41fc-87d7-67b4058914a8&prid=0&currency=INR&correlationId=d0809689-3f64-474f-8e66-6adf3d8b9264&analyticsSessionId=-4077541905147668620&pageTypeId=5&realLanguageId=16&languageId=1&origin=IN&cid=1844104&userId=f17c2e5d-d451-41fc-87d7-67b4058914a8&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=27&currencyCode=INR&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=sg-geoweb-6002&trafficGroupId=1&sessionId=2wsh4rawrsezb0j50r5xrd3e&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-03-19&priceCur=INR&textToSearch=Goa&travellerType=1&familyMode=off&hotelAccom=34&productType=-1')
# driver.get('https://www.agoda.com/en-gb/search?city=11304&hotelAccom=34')
driver.get('https://www.agoda.com/en-gb/search?guid=8c68d6d2-c5f3-4d9b-be0d-0ec0c2930736&asq=NQVGXW6jsE3tbdY9S%2BqUCpufa9Vwpz6XltTHq4n%2B9gPt6Sc9VYM%2BOtJvOdzFsuZ%2FQHsxV%2Fa6ZlGeW1yk89QKLVFcygV4CXzeo11i%2BlN77cvQXmAPCrT9hNstt6l21Ycz9qPZEWM%2BdOF7UNi91Yw4km0t3c82nJ%2Fp%2B0GXkwK5hQ84uUE8oRa1jEBYCfIz%2FxkbPTqQxhyYixfDuUGdcaLaFw%3D%3D&city=4923&tick=638139656038&locale=en-gb&ckuid=f17c2e5d-d451-41fc-87d7-67b4058914a8&prid=0&currency=INR&correlationId=4fa2b7ed-dca7-4ef0-9a92-85bbe6d2c3fe&analyticsSessionId=-4077541905147668620&pageTypeId=8&realLanguageId=16&languageId=1&origin=IN&cid=1844104&userId=f17c2e5d-d451-41fc-87d7-67b4058914a8&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=27&currencyCode=INR&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=sg-geoweb-6002&trafficGroupId=1&sessionId=2wsh4rawrsezb0j50r5xrd3e&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkIn=2023-03-18&checkOut=2023-03-19&rooms=1&adults=2&children=0&priceCur=INR&los=1&textToSearch=Bangalore&travellerType=1&familyMode=off&hotelAccom=34&productType=-1')
# driver.get('https://www.agoda.com/en-gb/search?guid=1c3cf3c4-7d65-48e8-8272-ac024ed99e8f&asq=NQVGXW6jsE3tbdY9S%2BqUCpufa9Vwpz6XltTHq4n%2B9gPt6Sc9VYM%2BOtJvOdzFsuZ%2FtOAgXtTcP7sMdWTylE%2BmQe6NnzqUBBQSZ%2Bb4J9jZmFJ9jt67hp2Tqpsm9hcBs1H9r6QDs48C6hOjLzuYUvlEgOm%2B3QacrQMDUE7JkJAfzu2S%2BkbeGiaj%2F0Qkj1CojC1jNefiiGOEfPaB%2FBBcMbJhAQ%3D%3D&city=16850&tick=638139651620&locale=en-gb&ckuid=f17c2e5d-d451-41fc-87d7-67b4058914a8&prid=0&currency=INR&correlationId=e01c7fba-a8ec-42f4-85a6-b8c8bbea937a&analyticsSessionId=-4077541905147668620&pageTypeId=8&realLanguageId=16&languageId=1&origin=IN&cid=1844104&userId=f17c2e5d-d451-41fc-87d7-67b4058914a8&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=27&currencyCode=INR&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=sg-geoweb-6001&trafficGroupId=1&sessionId=2wsh4rawrsezb0j50r5xrd3e&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkIn=2023-03-18&checkOut=2023-03-19&rooms=1&adults=2&children=0&priceCur=INR&los=1&textToSearch=Mumbai&travellerType=1&familyMode=off&hotelAccom=34&productType=-1')
# driver.get('https://www.agoda.com/en-gb/search?guid=d5981324-a70c-42a4-adeb-4727a62ca6ef&asq=Ss5PXyh1QUNdFOc4lzIDoPF%2BRvl%2F2EATmGvZScKd0zW3IquUAexOTl%2FhzaLZmWnRaWSjwIjTHvlb04caDPX%2BLSakxs82dlU7zKBDSJZAi9e%2FZ4YqbOAvOQvnlBpavpquvhQEJ9BZcQFQe0UWlQbb%2FnSk%2FM8eVuQYqDHVLhv%2F6oMlQbQkrodofQvoW4VW0Yf1SL39DmFShs2ly0VkfWYmtVur%2Ftc%2B54Iv4fnCDM4f8d8%3D&city=14552&tick=638139622330&locale=en-gb&ckuid=488910e7-02ce-4c63-9235-c136eba6333c&prid=0&currency=INR&correlationId=dc0c13a3-2c41-45a8-b9e9-80d0782c7ec3&analyticsSessionId=6754043375069554129&pageTypeId=1&realLanguageId=16&languageId=1&origin=IN&cid=-999&userId=488910e7-02ce-4c63-9235-c136eba6333c&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=27&currencyCode=INR&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=sg-pc-6f-acm-web-user-7f95bcdb66-wb8gx&trafficGroupId=4&sessionId=i55xawuiazafxy15fv2hxkhy&trafficSubGroupId=6&aid=178961&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkIn=2023-03-18&checkOut=2023-03-19&rooms=1&adults=2&children=0&priceCur=INR&los=1&textToSearch=New%20Delhi%20and%20NCR&travellerType=1&familyMode=off&hotelAccom=34&productType=-1')
# driver.get('https://www.agoda.com/en-gb/search?city=8801&checkIn=2023-03-17&los=1&rooms=1&adults=2&children=0&locale=en-gb&ckuid=0182c76e-8180-48f3-8d27-0c8ba23ac028&prid=0&currency=INR&correlationId=f69ac8bd-e451-4895-bc41-a873151fd889&analyticsSessionId=-4751410119102859786&pageTypeId=103&realLanguageId=16&languageId=1&origin=IN&cid=-1&userId=0182c76e-8180-48f3-8d27-0c8ba23ac028&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=27&currencyCode=INR&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=sg-pc-6g-acm-web-user-6c9ddbfd4f-wqvpl&trafficGroupId=4&sessionId=g5zvdddkpf2hqh0lhwzhajtt&trafficSubGroupId=4&aid=130243&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-03-18&priceCur=INR&textToSearch=Hyderabad&travellerType=1&familyMode=off&hotelAccom=34&productType=-1')
# driver.get('https://www.agoda.com/en-in/search?city=14552&checkIn=2023-03-17&los=1&rooms=1&adults=2&children=0&locale=en-in&ckuid=6de7850e-6a2c-43b1-ad6d-e351d852a0d4&prid=0&currency=INR&correlationId=09ef133d-192d-4d83-9b57-d68f1c056219&analyticsSessionId=2499185738723933123&pageTypeId=5&realLanguageId=15&languageId=1&origin=IN&cid=-999&userId=6de7850e-6a2c-43b1-ad6d-e351d852a0d4&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=27&currencyCode=INR&htmlLanguage=en-in&cultureInfoName=en-in&machineName=sg-geoweb-6002&trafficGroupId=4&sessionId=y0cwshtd4h2nvm0jgchz5ilg&trafficSubGroupId=6&aid=178961&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-03-18&priceCur=INR&textToSearch=New%20Delhi%20and%20NCR&travellerType=1&familyMode=off&hotelAccom=34&productType=-1')
# driver.get('https://www.agoda.com/en-gb/search?city=14552&hotelAccom=34')
driver.fullscreen_window()
for i in range(0,100):
    df = pd.DataFrame(columns=['links'])
    time.sleep(2)
    scroll_down(driver)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source , 'html.parser')

    table = soup.find('div', attrs = {'id':'contentContainer'})

    tt = table.findAll('ol' , attrs = {'class':'hotel-list-container'})
    nn =[]
    for e in tt:
        nn = e.findAll('li' , attrs = {'class':'PropertyCard PropertyCardItem'})

    a = []
    for ea in nn:
        temp = ea.findAll('a' , attrs={'class':'PropertyCard__Link'})
        a.append(temp)

    for e in a:
        temp_link = 'https://agoda.com'
        temp_link += e[0].attrs['href']
        links.append(temp_link)

    # if(i==0):
    time.sleep(2)
    btn = driver.find_element(By.ID ,'paginationNext')
    btn.click()

    time.sleep(2)


    print(links)
    print(len(links))
    for j in range(len(links)):
        df.loc[len(df.index)] = [links[j]]
    df.to_csv('bangalore_hotel_links.csv')



driver.close()





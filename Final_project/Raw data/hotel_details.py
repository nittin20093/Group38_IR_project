import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# import requests
from bs4 import BeautifulSoup
# from selenium.webdriver.common.action_chains import ActionChains

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

df_details = pd.DataFrame(columns=['details'])

df = pd.read_csv('./delhi_ncr_all_links_new.csv')

urls = list(df['links'])
# urls = urls[631:]
# all_urls = list(df['links'])

# urls_idxs = [17, 18, 24, 26, 34, 36, 39, 48, 49, 53, 55, 64, 81, 90, 99, 110, 116, 121, 124, 133, 142, 154, 158, 167, 195, 204, 213, 222, 233, 238, 247, 256, 256, 268, 272, 291, 297, 299, 311, 315, 318, 320, 320, 321, 323, 329, 347, 349, 349, 350, 352, 352, 356, 368, 371, 376, 378, 384, 393, 402, 413, 418, 418, 427, 446, 446, 451, 460, 460, 469, 471, 473, 475, 475, 503, 503, 503, 508, 509, 516, 517]
# urls = list()

# for eac in urls_idxs:
#     urls.append(all_urls[17])



# print(urls)

# exit()

idx = 0
idx_list = list()
non_idx_list = list()
rating_crash = list()

for url in urls:
    print('start->')
    print(idx_list)
    print(non_idx_list)
    print(rating_crash)

    driver = webdriver.Safari()

    driver.get(url)
    # driver.get('https://agoda.com/en-gb/the-zuri-whitefield-bangalore/hotel/bangalore-in.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2023-03-18&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=INR&isFreeOccSearch=false&isCityHaveAsq=false&los=1&searchrequestid=fedc1d8f-f788-4eb5-94f4-f1651748d48b')
    # driver.get('https://agoda.com/en-gb/hotel-suba-international/hotel/mumbai-in.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2023-03-18&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=INR&isFreeOccSearch=false&isCityHaveAsq=false&tspTypes=-1&los=1&searchrequestid=f9fe520c-9d43-49f8-8a47-37310cf820fa')

    # driver.get('https://www.agoda.com/en-gb/the-elanza-hotel/hotel/bangalore-in.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2023-03-18&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=INR&isFreeOccSearch=false&isCityHaveAsq=false&los=1&searchrequestid=fedc1d8f-f788-4eb5-94f4-f1651748d48b')
    # driver.get('https://www.agoda.com/en-gb/phoenix-hotels-resorts-by-omatra/hotel/bangalore-in.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2023-03-18&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=INR&isFreeOccSearch=false&isCityHaveAsq=false&tspTypes=9,9&los=1&searchrequestid=5c63b06f-e45b-43ee-8224-048b4481959d')
    driver.fullscreen_window()
    time.sleep(5)

    details = dict()

    soup = BeautifulSoup(driver.page_source , 'html.parser')
    # time.sleep(20)
    # hotel_name = soup.find('p' , attrs = {'class':'HeaderCerebrum__AdaName'}).get_text()
    # hotel_name = driver.find_element(By.XPATH , "//h1[@data-selenium='hotel-header-name']").text

    # hotel_full_address = soup.find('span' , attrs = {'class':'Spanstyled__SpanStyled-sc-16tp9kb-0 gwICfd kite-js-Span HeaderCerebrum__Address'}).get_text()
    hotel_full_address = driver.find_elements(By.XPATH , "//span[@class='Spanstyled__SpanStyled-sc-16tp9kb-0 gwICfd kite-js-Span HeaderCerebrum__Address']")
    # print('Hotel Name :' , hotel_name)
    # print('Hotel Full Address/Location :' , hotel_full_address)
    if(len(hotel_full_address)!=0):
        details['Location'] = hotel_full_address[0].text
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue



    # overall_rating = driver.find_elements(By.XPATH , "//h4[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 gouaKT kite-js-Typography ']")
    # # overall_rating = driver.find_element(By.XPATH , "//div[@class='CombinedReview__OverallRating'][@data-element-name='review-overall-rating']").find_element(By.TAG_NAME , 'h3')
    # # print('overall rating :' , overall_rating.text)
    # if(len(overall_rating)!=0):
    #     details['overall_rating'] = overall_rating[0].text
    # else:
    #     driver.close()
    #     non_idx_list.append(idx)
    #     continue


    # logo = driver.find_element()


    # scroll_down(driver)
    time.sleep(0.1)

    scrl = driver.find_elements(By.CLASS_NAME ,'MasterRoom-infoSeePhotos')
    if(len(scrl) != 0):
        driver.execute_script("arguments[0].scrollIntoView();", scrl[0])
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue
    
    time.sleep(0.1)
    scrl = driver.find_elements(By.ID , 'property-room-grid-root')
    if(len(scrl) != 0):
        driver.execute_script("arguments[0].scrollIntoView();", scrl[0])
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue
    
    time.sleep(0.1)
    scrl = driver.find_elements(By.ID , 'reviewSection')
    if(len(scrl) != 0):
        driver.execute_script("arguments[0].scrollIntoView();", scrl[0])
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue
    
    time.sleep(0.1)
    scrl = driver.find_elements(By.XPATH , "//select[@id='review-sort-id']/option[@value='1']")
    if(len(scrl) != 0):
        driver.execute_script("arguments[0].scrollIntoView();", scrl[0])
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue
    
    time.sleep(0.5)

    overall_rating = driver.find_elements(By.XPATH , "//div[@class='ReviewScore-Number ReviewScore-Number--line-height']")
    # overall_rating = driver.find_element(By.XPATH , "//div[@class='CombinedReview__OverallRating'][@data-element-name='review-overall-rating']").find_element(By.TAG_NAME , 'h3')
    # print('overall rating :' , overall_rating.text)
    if(len(overall_rating)!=0):
        details['overall_rating'] = overall_rating[0].text
    else:
        overall_rating = driver.find_elements(By.XPATH , "//h3[@class='Typographystyled__TypographyStyled-sc-j18mtu-0 hTkvyT kite-js-Typography ']")
        if(len(overall_rating)!=0):
            details['overall_rating'] = overall_rating[0].text
        else:
            driver.close()
            non_idx_list.append(idx)
            rating_crash.append(idx)
            idx += 1
            continue



    # ActionChains(driver).move_to_element(driver.find_element(By.CLASS_NAME , 'RoomGrid-titleCountersText')).perform()
    # time.sleep(2)



    # temp = driver.find_element(By.XPATH , "//li[@data-element-name='customer-reviews-panel-navbar-menu']").click()
    # temp.find_element(By.XPATH , "//button[@role='menuitem']").click()


    # driver.find_element(By.CLASS_NAME , 'ReviewBadge-description-title').click()

    # time.sleep(4)

    # overall_rating = driver.find_element(By.XPATH , "//div[@data-selenium='hotel-header-review-score']")

    # jhgfdsghjkhgfxcghjhgcv


    # reviews_btn = driver.find_element(By.XPATH , "//li[@data-element-name='customer-reviews-panel-navbar-menu']").find_element(By.XPATH , "//button[@class='sc-bdfBwQ sc-gsTCUz  cChcDw']")
    # # print(reviews_btn)
    # reviews_btn.click()
    # time.sleep(2)


    # driver.find_element(By.XPATH , "//div[@class='ReviewScoreCompact']").click()
    # time.sleep(1)


    # ActionChains(driver).move_to_element(driver.find_element(By.CLASS_NAME , 'RoomGrid-titleCountersText')).perform()
    # # ActionChains(driver).move_to_element(driver.).perform()
    # time.sleep(2)

    hotel_name_h2 = driver.find_elements(By.XPATH , "//h2[@class='Heading-overlay-text']")
    if(len(hotel_name_h2)!=0):
        hotel_name = hotel_name_h2[0].find_elements(By.XPATH , "//span[@class='Heading-hotelname']")
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue
    
    if(len(hotel_name)!=0):
        details['Name'] = hotel_name[0].text
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue
    
    sort_reviews_dropdown = driver.find_elements(By.XPATH , "//select[@id='review-sort-id']/option[@value='1']")
    if(len(sort_reviews_dropdown)!=0):
        sort_reviews_dropdown[0].click()
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue

    time.sleep(2)

    all_reviews = driver.find_elements(By.ID , 'reviewSectionComments')
    if(len(all_reviews)!=0):
        reviews_destructured = all_reviews[0].find_elements(By.CLASS_NAME , 'Review-comment')
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue
    
    # i = 1
    if(len(reviews_destructured)==0):
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue

    all_reviews_list = list()
    for e in reviews_destructured:
        review = dict()
        # print('-----------------------------------------------------------------------------------------------------------------------------------------------')
        # print('Review',i,":")
        # print( 'Review_Rating :' , e.find_element(By.CLASS_NAME , 'Review-comment-leftScore').text)
        if(len(e.find_elements(By.CLASS_NAME , 'Review-comment-leftScore'))!=0):
            review['Review_Rating'] = e.find_element(By.CLASS_NAME , 'Review-comment-leftScore').text
        else:
            driver.close()
            non_idx_list.append(idx)
            idx += 1
            continue
        if(len(e.find_elements(By.CLASS_NAME , 'Review-comment-bodyTitle'))!=0):
            review['Review_Heading'] = e.find_element(By.CLASS_NAME , 'Review-comment-bodyTitle').text
        else:
            driver.close()
            non_idx_list.append(idx)
            idx += 1
            continue
        if(len(e.find_elements(By.CLASS_NAME , 'Review-comment-bodyText'))!=0):
            review['Review_Body'] = e.find_element(By.CLASS_NAME , 'Review-comment-bodyText').text
        else:
            driver.close()
            non_idx_list.append(idx)
            idx += 1
            continue
        all_reviews_list.append(review)
        # i += 1

    details['reviews'] = all_reviews_list    


    # driver.close()
    # exit()

    btn = driver.find_elements(By.CLASS_NAME ,'MasterRoom-infoSeePhotos')
    if(len(btn) != 0):
        btn[0].click()
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue

    time.sleep(4)


    price_outerdiv_ele = driver.find_elements(By.XPATH , "//div[@data-element-name='hotel-gallery-price']")
    if(len(price_outerdiv_ele)!=0):
        price_ele = price_outerdiv_ele[0].find_elements(By.XPATH , "//span[@data-section='price']")
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue

    if(len(price_ele)!=0):
        details['price'] = price_ele[0].text
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue



    img = driver.find_elements(By.XPATH , "//img[@data-element-name='room-gallery-display-photo']")
    # btn = driver.find_elements(By.XPATH , "//div[@data-component='image-wrapper']")
    if(len(img)!=0):
        # print("image :",str(img[0].get_attribute('src')))
        details['img_link'] = str(img[0].get_attribute('src'))
    else:
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue

    amenties_list = list()
    amenties = driver.find_elements(By.XPATH , "//div[@class='Box-sc-kv6pi1-0 eTRaaK']")

    if(len(amenties)==0):
        driver.close()
        non_idx_list.append(idx)
        idx += 1
        continue

    details['room_size'] = '0'
    for e in amenties:
        # print("amenities: " , e.text)
        if(e.text.split(' ')[0]=='Room' and e.text.split(' ')[1]=='size:'):
            details['room_size'] = str(e.text.split(' ')[2]) + 'm²'
            continue
        if('bed' in e.text.split(' ')):
            continue
        amenties_list.append(e.text)

    details['amenities'] = amenties_list

    # time.sleep(2)

    details['city'] = 'Delhi NCR'

    # print(details)
    print(idx)
    idx_list.append(idx)
    idx+=1

    time.sleep(0.5)


    driver.close()  

    # for j in range(len(links)):
    details['link'] = url
    df_details.loc[len(df_details.index)] = [details]
    df_details.to_csv('delhi_ncr_hotel_details.csv')

    print('end->')
    print(idx_list)
    print(non_idx_list)
    print(rating_crash)

    time.sleep(0.5)

print('out->')
print(idx_list)
print(non_idx_list)
print(rating_crash)
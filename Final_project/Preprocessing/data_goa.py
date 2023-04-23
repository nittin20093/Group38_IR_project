import pandas as pd
import json
import ast
from collections import OrderedDict
import numpy as np

df = pd.read_csv('./goa_hotel_details.csv')
# print(df)
all_dic=[]
all_keys=[]
loc=[]
rat=[]
name=[]
rev=[]
price=[]
img=[]
rmsize=[]
amen=[]
city=[]
link=[]
i=0
li = list()
while i<len(df['details']):
    dic=df.loc[i].at["details"]
    # print(type(dic))
    # d = json.loads('"'+dic+'"')
    p = ast.literal_eval(dic)
    # i+=1
    # continue
    # print(p)
    for key, value in p.items():
        if key not in all_keys:
            all_keys.append(key)
    
    loc.append(p['Location'])
    rat.append(p['overall_rating'])
    name.append(p['Name'])
    rev.append(p['reviews'])
    price.append(p['price'])
    img.append(p['img_link'])
    rmsize.append(p['room_size'])
    am=p['amenities']
    # print("am is ", am)
    # print("len of am is ", len(am))
    
    am1=[]


    
    for o in range(len(am)):
        if am[o].__contains__('bed'):
            continue
        else:
            am1.append(am[o])
    
    # print(am1)
    # print("len of am1", len(am1))
    # break

    for m in range(len(am1)):
        # print(am[m])
        if am1[m] ==  'Complimentary Wi-Fi' or am1[m]== 'Wi-Fi available in all rooms' or am1[m]== 'Free Wi-Fi in all rooms':
            am1[m]='Free Wi-Fi'
        if am1[m] =='AC' :
            am1[m]='Air conditioning'
        if am1[m] =='Smoke-free' :
            am1[m]='Non-smoking'
        if am1[m] =='Shower cabin'  :
            am1[m]='Bathroom with shower'
        if am1[m] =='Swimming pool' or am1[m]=='Pool facilities'  :
            am1[m]='Pool'
        if am1[m] =='Cable TV' or am1[m]=='Satellite TV' or am1[m]=='Cable channels' or am1[m]=='Satellite' or am1[m]=='Television' or am1[m]=='Satellite' :
            am1[m]='TV'
        if am1[m] =='Ceiling fan' :
            am1[m]='Fan'
        if am1[m] =='Complimentary toiletries' :
            am1[m]='Toiletries' or am1[m]=='Cleaning supplies' or am1[m]=='Cleaning products'
        if am1[m] =='Bath towels' :
            am1[m]='Towels'
        if am1[m] =='Hand disinfectant'    :
            am1[m]='Hand sanitzer'
        if am1[m] =='Wake-up service'    :
            am1[m]='Wake-up call'
        if am1[m] =='Coffee'  or am1[m]=='Coffee machine' or am1[m]=='tea making facilities':
            am1[m]='Tea and coffee maker'
        if am1[m] =='Safety features'  or am1[m]=='Security features':
            am1[m]='TSafety and security features'
        if am1[m] =='Free bottled water'    :
            am1[m]='Complimentary bottled water'
        if am1[m] =='Desk'    :
            am1[m]='Work desk'
        if  am1[m]=='Outdoor seating'   :
            am1[m]='Outdoor furniture'

        if  am1[m]=='Bed linens'   :
            am1[m]='Linens'

        if  am1[m]=='Seating area'   :
            am1[m]='Lounge area'
        if  am1[m]=='Telephone'   :
            am1[m]='Phone'
        if  am1[m]=='Room darkening curtains'   :
            am1[m]='Blackout curtains'
        if  am1[m]=='Ironing facilities'   :
            am1[m]='Iron'
        if  am1[m]=='Hairdryer'   :
            am1[m]='Blow dryer'
        if  am1[m]=='Hotel concierge'   :
            am1[m]='Concierge'
        if  am1[m]=='Sleep-enhancing amenities'   :
            am1[m]='Sleep comfort items'
        if  am1[m]==' Soundproofing'   :
            am1[m]='Soundproof windows'
        if  am1[m]=='Refrigerator'   :
            am1[m]='Fridge'
        if  am1[m]=='In-room safe box'  or am1[m]=='Locker' or am1[m]=='Personal locker' :
            am1[m]='Safe deposit box'
        if  am1[m]=='Refrigerator'   :
            am1[m]='Fridge'
        if  am1[m]=='Refrigerator'   :
            am1[m]='Fridge'
            
        if  am1[m]=='Waste basket'   :
            am1[m]='rash cans'
        if  am1[m]=='Wardrobe'   :
            am1[m]='Closet'
        if  am1[m]=='ndividual climate control'   :
            am1[m]='Individual air conditioning'
        if  am1[m]=='Seating area'   :
            am1[m]='Lounge area'

        if am1[m] ==  '10 bathrooms' or am1[m]=='Shared bathroom' or am1[m]=='Additional bathroom' or am1[m]=='13 bathrooms' or am1[m]=='19 bathrooms' :
            am1[m]='Bathroom'
            print(am[m])
        
        
    
    
            # print(am[m])
        # print(am[m])
    amen.append(am1)
    city.append(p['city'])
    link.append(p['link'])
    i+=1

    # for i in key:
    #     x=key[i]
    #     print(x)
# m=0
# while m <= len(amen):
#     if amen[m]== "Free Wi-Fi" or "Free Wi-Fi in all rooms!" or "Wi-Fi [free]" or "Mobile hotspot device":
#             amen[m]="Free Wi-Fi"
#     m=m+1
# print("amen is \n", amen)
# for m in range(len(amen)):
#         print("amen[m] is",  amen[m])
#         if amen[m]== "Free Wi-Fi" or "Free Wi-Fi in all rooms!" or "Wi-Fi [free]" or "Mobile hotspot device":
#             amen[m]="Free Wi-Fi"
# print(loc)
# print(rat)
# print(name)
# print(rev)
# print(price)
# print(img)
# print(rmsize)
# print(amen)
# print(city)
# print(link)

# exit()

df['Location']=loc
df['overall_rating']=rat
df['Name']=name
df['reviews']=rev
df['price']=price
df['img_link']=img
df['room_size']=rmsize
df['amenities']=amen
df['city']=city
df['link']=link
# print(df)
# df['Free Wifi']  = li

# print("1 amen", amen)
total_amenities=[]
l = 0
while l < len(amen):
    for j in amen[l]:
        if j not in total_amenities:
            total_amenities.append(j)
    l = l + 1

# l=0
# while l <= len(amen):
#     for j in amen[l]:
#         if j not in total_amenities:
#             total_amenities.append(j)
#         l=l+1
# print("2 amen", amen)
print(total_amenities)
print(len(total_amenities))
# df[total_amenities[0]] 



# print(df['amenities'][5])
for each_amenity in total_amenities:
    li_val = list()
    for i in range(len(df)):
        # print(p['amenities'])
        if(each_amenity in df['amenities'][i]):
            li_val.append(1)
        else:
            li_val.append(0)
    df[each_amenity] = li_val

    # print(df['Location'])

df.to_csv('goa_hotels_details_final.csv')








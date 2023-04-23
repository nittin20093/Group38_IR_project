import pandas as pd
import json
import ast
from collections import OrderedDict
import numpy as np

df = pd.read_csv('./delhi_ncr_hotel_details_ghr.csv')
print(df)
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
    
    am1=[]

    
    for o in range(len(am)):
        if am[o].__contains__('bed'):
            continue
        else:
            am1.append(am[o])
    
    # print(am)

    for m in range(len(am1)):
        # print(am[m])
        if am1[m] ==  'Free Wi-Fi in all rooms!' or am1[m]=='Free Wi-Fi' or am1[m]=='Wi-Fi [free]' or am1[m]=='Mobile hotspot device' or am1[m]=='Internet access – wireless' or am1[m]=='Internet access – LAN':
            am1[m]='Free Wi-Fi'
        if am1[m] =='Individual air conditioning' :
            am1[m]='Air conditioning'
        if am1[m] =='Alarm clock telephone ringer' :
            am1[m]='Alarm clock'
        if am1[m] =='Walk-in shower' or am1[m]=='Shower and bathtub' or am1[m]=='Roll-in shower'  :
            am1[m]='Shower'
        if am1[m] =='TV [flat screen]' or am1[m]=='Satellite/cable channels' or am1[m]=='TV [in bathroom]' or am1[m]=='Close-caption TV,' or am1[m]=='Blu-ray player' :
            am1[m]='TV'
        if am1[m] =='Pajamas' :
            am1[m]='Sleep comfort items'
        if am1[m] =='Cleaning products' :
            am1[m]='Toiletries'
        if am1[m] =='Clothes rack' :
            am1[m]='closet'
        if am1[m] =='Laptop workspace'    :
            am1[m]='Desk'
        if  am1[m]=='Seating area'   :
            am1[m]='sofa'
        if am1[m] ==  '10 bathrooms' or am1[m]=='Shared bathroom' or am1[m]=='Additional bathroom' or am1[m]=='13 bathrooms' or am1[m]=='19 bathrooms' :
            am1[m]='Bathroom'
            # print(am[m])
        
        
    
    
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
# print(len(total_amenities))
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

df.to_csv('delhi_hotels_details_final.csv')








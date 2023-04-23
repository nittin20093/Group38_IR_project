import urllib.request
from PIL import Image


def getpath(index,city):
  path="./home/images/"
  path=path+ str(index)+'.jpg'
  return path

def downloadImagelink(filepath):
  
  count=0
  file = open(filepath,"r")
  for hotel in file:
      # print(hotel)
      if(count==0):
        count=count+1
        continue
      pa="img_link"
      pathend='room_size'
      comma=hotel.index(',')
      index=hotel[:comma]
      x=hotel.index(pa) + 12
      y=hotel.index(pathend)-4
      imglink=hotel[x:y]
      path=getpath(index,'banglore')
      print(imglink)
      try:
        urllib.request.urlretrieve(imglink,path)
      except:
        continue
      count=count+1
  file.close()
    

downloadImagelink('./home/banglore_hotels_details_final_freq.csv')
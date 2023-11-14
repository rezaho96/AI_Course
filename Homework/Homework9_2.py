import requests
from bs4 import BeautifulSoup
import json


res=requests.get("https://www.entekhabcenter.com/product-category/product/audio-video/television")
soup=BeautifulSoup(res.content,"html.parser")
items_price=soup.select("div.prodcut-price.has-perc.mt-2.d-flex.align-items-center.position-relative > del")
# items=soup.select("div.prodcut-price.has-perc.mt-2.d-flex.align-items-center.position-relative > ins")
items_name=soup.select("div.sec-2-p > a > h5")
list_name=[]
for item in items_name:
    list_name.append(item.text)
list_price=[]
for item in items_price:
    list_price.append(item.text)

indx=0
list_commodit=[]
for item in range(12):
    commodit={}
    
    if indx < 9:
       commodit["Name"]=list_name[indx]
       commodit["Price"]=list_price[indx]
    else:
        commodit["Name"]=list_name[indx]
        commodit["Price"]="ناموجود"
    list_commodit.append(commodit)
    indx+=1
print(list_commodit)
with open("Homework\\file1.json","w") as file1:
        json.dump(list_commodit,file1,indent=4) 
    
    
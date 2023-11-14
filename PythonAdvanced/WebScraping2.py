import requests
from bs4 import BeautifulSoup

# res=requests.get("https://darsman.com")
# soup=BeautifulSoup(res.content,"html.parser")
# # print(soup.body)
# img_list=soup.find_all("img")
# print(img_list)
# for img in img_list:
#     print(img["src"])



res=requests.get("https://www.entekhabcenter.com/product-category/product/audio-video/television")
soup=BeautifulSoup(res.content,"html.parser")
# print(soup.select("style"))
items=soup.select("a")
for item in items:
    print(item)
for item in items:
    print(item["href"])


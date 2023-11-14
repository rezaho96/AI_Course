import requests
from bs4 import BeautifulSoup

# res=requests.get("https://www.entekhabcenter.com/product-category/product/audio-video/television")
# soup=BeautifulSoup(res.content,"html.parser")
# items=soup.select("div.sec-2-p > a > h5")
# print(len(items))
# for item in items:
#     print(item.text)
# res=requests.get("https://www.entekhabcenter.com/product-category/product/audio-video/television")
# soup=BeautifulSoup(res.content,"html.parser")
# items=soup.select("div.prodcut-price.has-perc.mt-2.d-flex.align-items-center.position-relative > del")
# print(len(items))
# for item in items:
#     print(item.text)
# res=requests.get("https://www.entekhabcenter.com/product-category/product/audio-video/television")
# soup=BeautifulSoup(res.content,"html.parser")
# items=soup.select("div.prodcut-price.has-perc.mt-2.d-flex.align-items-center.position-relative > ins")
# print(len(items))
# for item in items:
#     print(item.text)
res=requests.get("https://www.entekhabcenter.com/product-category/product/audio-video/television")
soup=BeautifulSoup(res.content,"html.parser")
items=soup.select(" div.sec-2-p > div > b")
print(len(items))
for item in items:
    print(item.text)
    #p-84781 > div > div > div > div.sec-2-p > div > b
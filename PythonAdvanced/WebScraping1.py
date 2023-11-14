import requests
import re


res = requests.get("https://Yahoo.com/")
print(res.status_code)
# print(res.text)
print(re.findall(r"<title>.*</title>",res.text))
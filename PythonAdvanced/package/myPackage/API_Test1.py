from myPackage  import requests

parameters={"country":"IRAN"}
response = requests.get("http://universities.hipolabs.com/search?",parameters)


if response.status_code==200:
    res_json=response.json()
else:
    print("Error :" , response.status_code)


print(res_json[0]["name"])




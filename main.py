from more_itertools import only
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

payload = "{}"
response = requests.request("GET", url, data=payload)

ids = response.text
# print(ids)

for i in ids:
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(i) + ".json"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    content = response.read[:100]
    ''' print only  content title and url '''   
    
 

    # print("\n")
    
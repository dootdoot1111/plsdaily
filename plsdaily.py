import requests

url =  "https://discord.com/api/v9/channels/<you channel id here>"

header = {"authorization" : "your secret key here"}

payload = {"content" : "pls daily"}

requests.post(url, headers=header, data=payload)

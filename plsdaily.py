import requests

url =  "https://discord.com/api/v9/channels/839474281201008650/messages"

header = {"authorization" : "mfa.GXVR1Y8tnT6n3KV0iCv2zmowMf40qe2kk18kkyqL60mfiJrmCcbCfN3JoBeqWIB0gXDUiidWsANgXnoQBshN"}

payload = {"content" : "pls daily"}

requests.post(url, headers=header, data=payload)

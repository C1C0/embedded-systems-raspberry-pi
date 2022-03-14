import requests
import time

code = """Wrong message, I meant to be nice. Just playing out with webhooks."""

url = 'https://discord.com/api/webhooks/952836404549910579/zcZsyR_Z_f_DZklMTYZMuyCqu-NiPlFauWAeAd5bQTP68wVtewL23dhdS2PdJe986Q9D'
myobj = {'content': code}

while True:
    x = requests.post(url, data = myobj)
    time.sleep(.5)
    

# print(x.text)
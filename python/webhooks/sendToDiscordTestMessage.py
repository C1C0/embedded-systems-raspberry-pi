import requests
import time

code = """Wrong message, I meant to be nice. Just playing out with webhooks."""

url = 'https://maker.ifttt.com/trigger/test/json/with/key/ZKLn-fkqaQdl58NJvHNUP'
myobj = {'content': code}

while True:
    x = requests.post(url, data = myobj)
    time.sleep(.5)
    

# print(x.text)
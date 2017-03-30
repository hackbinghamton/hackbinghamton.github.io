import requests
from bs4 import BeautifulSoup

url ="https://github.com/jackfischer"

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
img = soup.find(class_="avatar")

imageurl = img.attrs["src"]
resp = requests.get(imageurl)

f = open("imagewoo.png", 'wb')
for b in resp:
  f.write(b)



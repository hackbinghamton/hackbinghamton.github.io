import requests
from bs4 import BeautifulSoup

#We looked at how the URL for the search is created,
#it's this with the desired word added to 'term='
base_url = "http://www.urbandictionary.com/define.php?term="
word = "binghamton"

#Perform a get request to the overall URL with the python requests library
request = requests.get(base_url + word)
#Extract the string body of the response
html = request.content

#Instantiate our BS parser with the HTML and the kind of parser we want to use
soup = BeautifulSoup(html, "html.parser")
#Look for the element with class 'meaning' from examining the page
#We want the text from that div
definition = soup.find(class_="meaning").text


print(definition.strip()) #strip() gets rid of extra white space


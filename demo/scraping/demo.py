import requests
import bs4

url = 'http://itaiferber.net'
document = requests.get(url).content
soup = bs4.BeautifulSoup(document, 'html.parser')

print('HTML:')
print(soup)

input()
print('BIO:')
print(soup.find(id='bio'))


input()
print('LINKS:')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

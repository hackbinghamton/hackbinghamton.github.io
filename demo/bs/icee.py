from bs4 import BeautifulSoup
import requests

"""
Extract ALL of the locations from Icee's website via this page
http://www.icee.com/locationsICEE.asp
"""

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for state in states:
  stateselection = "http://www.icee.com/locationsICEE.asp?state=%s" % state
  r = requests.get(stateselection)
  soup = BeautifulSoup(r.text, "html.parser")
  rows = soup.find_all("option")
  cities = [row.attrs['value'] for row in rows]

  for city in cities:
    data = {'city': city, 'state': state, 'submit': 'submit'}
    url = "http://www.icee.com/locationsresults.asp"
    r = requests.get(url, data=data)
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.find_all(class_="order_table2")
    i = 6
    while i < len(rows):
      print(rows[i].text + rows[i+1].text)
      i += 4


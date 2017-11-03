import requests as rq
import datetime as dt

def main():
    
    url = 'https://httpbin.org'
    payload = {'hack': 'bu'}

    r = rq.get(url, params=payload)
    print(r.text)
    print(r.url)
    
    r2 = rq.post('https://httpbin.org/post', data=payload)
    print(r2.json())
    
    #Get data from EQX website
    today = dt.date.today()
    today = today.strftime("%m/%d/%Y")

    time = "8:00am"
    url2 = "http://www.weqx.com/song-history/"
    payload = {'playlisttime': time, 'playlistdate':today, 'submitbtn': 'Update'}
    r3 = rq.post(url2, payload)
    print(r3.text)

main()

from bs4 import BeautifulSoup
import requests 
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
link = soup.select('.titleline > a')
link2 = soup2.select('.titleline > a')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
big_link = link + link2
big_subtext = subtext + subtext2

def sort_hn(list):
    return sorted(list, key= lambda k: k['votes'], reverse= True)

def cust_hn(link, vote):
    hn = []
    for ids, item in enumerate(link):
        title = item.getText()
        href = item.get('href', None)
        vote = big_subtext[ids].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'Title': title, 'link': href, 'votes': points})
    return sort_hn(hn)

pprint.pprint(cust_hn(big_link, big_subtext))
from typing import List, Any

from bs4 import BeautifulSoup as bs
import requests
import pprint
r=requests.get("https://news.ycombinator.com/news")
soup=bs(r.content,'lxml')
#print(soup)
#print(soup.prettify())
#print(len(soup.body.contents))
scores=soup.find_all('span',attrs={'class':'score'})
link=soup.select('.storylink')
def sortlist(hackernews):
    ans=sorted(hackernews,key=lambda x:x['scores'],reverse=True)
    return ans

def hackernews(links,scores):
    a=[]

    for i,j in enumerate(links):
        title=links[i].get_text()
        links_title=links[i]['href']
        up_scores=int(scores[i].string.replace("points",''))
        if up_scores>=100:
         a.append({'title':title,'links':links_title,'scores':up_scores})

    return sortlist(a)
pprint.pprint((hackernews(link,scores)))








import requests
from bs4 import BeautifulSoup as bs
website=requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup=bs(website.content,'lxml')
#print(soup.prettify())
webpage=soup.find_all('a')
c=[]
for i in range(1,6):
    c.append(webpage[i]['href'])
#print(c)
webpage1=soup.select('ul.socials a')
d=[]
for i in webpage1:
    d.append(i['href'])
#print(d)
webpage2=soup.find('ul',attrs={'class':'socials'})
#print(webpage2)
webpage3=soup.select('li.social a')
#print(webpage3)
table=soup.select('table.hockey-stats')
#print(table)
table1=soup.find('table',attrs={'class':'hockey-stats'})

import pandas as pd
final=table1.find_all('th')
final=[i.string for i in final]
#print(final)
row=table1.find('tbody').find_all('tr')
rows=[]
for i in row:
    td=i.find_all('td')
    a=[str(tr.get_text()).strip() for tr in td]
    rows.append(a)
#print(rows)
df=pd.DataFrame(rows,columns=final)
#print(df)

website4=soup.find('ul',attrs={'class':'fun-facts'})
website5=website4.find_all('li')
website5=[i.get_text() for i in website5 if 'is' in i.get_text()]
print(website5)
import requests
from bs4 import BeautifulSoup as bs

# Loading the webpage content
r=requests.get("https://keithgalli.github.io/web-scraping/example.html")
# Converting it to a beautiful soup object
soup=bs(r.content,"lxml")

#print(soup)
print(soup.prettify())
#find and find_all
head2=soup.find(['body','title'])
#print(head2)
head3=soup.find_all('p',attrs={"id":"paragraph-id"})
#print(head3)
# To find string
search=soup.find_all('p',text='Some bold text')
#print(search)
# Not ideal so use regex
import re
search1=soup.find_all('p',text=re.compile('Some'))
print(search1)
# Use of CSS selector
new1=soup.select('div p')
print(new1)
new2=soup.find('h2')
print(new2.string)
new3=soup.find('a')
print(new3.string)
new4=soup.find('div')
print(new4.prettify())
print(new4.get_text())
print(new3['href'])
print((soup.body).find('div').find_next_siblings())
print(soup.body.find_parent())
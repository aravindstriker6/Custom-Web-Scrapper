from bs4 import BeautifulSoup as bs
import requests
import pprint

r = requests.get("https://news.ycombinator.com/news")
soups = [bs(r.content, 'lxml')]
ans = int(input("How many more pages do u want to scrape: "))
for i in range(2, ans + 2):
    r = requests.get("https://news.ycombinator.com/news?p=" + str(i))
    soup = bs(r.content, 'lxml')
    soups.append(soup)


def combination(soups):
    subtext = []
    link = []
    for j in (soups):
        sub = j.select('.subtext')
        links = j.select('.storylink')
        subtext.append(sub)
        link.append(links)
    return subtext, link


subtext, link = combination(soups)


def mega_combiner(lists):
    s = []
    for i in lists:
        s = s + i
    return s


mega_subtext = mega_combiner(subtext)
mega_link = mega_combiner(link)


def sortlist(hackernews):
    ans = sorted(hackernews, key=lambda x: x['scores'], reverse=True)
    return ans


def hackernews(links, scores):
    a = []

    for i, j in enumerate(links):
        title = links[i].get_text()
        links_title = links[i]['href']
        points = mega_subtext[i].select('.score')
        if len(points):
            up_scores = int(points[0].string.replace("points", ''))
            if up_scores >= 100:
                a.append({'title': title, 'links': links_title, 'scores': up_scores})

    return sortlist(a)


pprint.pprint((hackernews(mega_link, mega_subtext)))
print(f"All news with scores above 100 has been scrapped and the best news that we have found out is {hackernews(mega_link, mega_subtext)[0]['title']} . The news has got {hackernews(mega_link, mega_subtext)[0]['scores']} votes which is really good. The link to the news is: {hackernews(mega_link, mega_subtext)[0]['links']}.Please read and share the news. ")

import requests
from bs4 import BeautifulSoup
import re
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')
moreLinks = soup.select('.morelink')
print(moreLinks)


def sort_news(hacknews_list):
    return  sorted(hacknews_list, key= lambda k:k['votes'], reverse=True)


def custom_hackernews(links, subtext):
    hacknews = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hacknews.append({'title' : title, 'link' : href, 'votes': points})
    return  sort_news(hacknews)

pprint.pprint(custom_hackernews(links, subtext))
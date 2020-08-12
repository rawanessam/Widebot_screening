#Name: Rawan Essam
#Email:rawanessam34@gmail.com

import requests_html
import bs4
from time import sleep


history = []  # list of links that are already visted
no_links = 0  # Binary variable to check whether a page with no normal links is reached
is_looping = 0  # Binary variable to check whether the function started to loop and revisit links


def getArticleBody(
        url):  # Takes url to a wikipage as an input retuns a list of all the paragraph tags in a Wiki article
        session = requests_html.HTMLSession()
        wikiPage = session.get(url)
        wikiHtml = bs4.BeautifulSoup(wikiPage.text, 'html.parser')
        body = wikiHtml.find_all(id='mw-content-text')[0]
        bodyText = body.find_all('p')
        return bodyText


def goToNextPage(url):  # Navigates to the first normal link in the article body
    bodyText=getArticleBody(url)
    for p in bodyText:
            links = p.find_all('a', recursive=False)  # a list of all the hyper links in a paragraph

            for link in links:
                if 'href' in link.attrs.keys():
                    url = 'https://en.wikipedia.org' + link['href']

                    if 'class' not in link.attrs.keys() and '(page does not exist)' not in link['title']:  # checking that a
                        # link is not external nor to a non esistant page

                        print(url)
                        return url
                        break

    no_links = 1

#Evaluating Getting Philosophy low
url = 'https://en.wikipedia.org/wiki/Cisy,_Bytów_County'

cnt=0
while url !='https://en.wikipedia.org/wiki/Philosophy' and url not in history and no_links==0:
    history.append(url)
    nextPage = goToNextPage(url)
    url = nextPage

    cnt+=1
    print(history)
    sleep(5)
if url == 'https://en.wikipedia.org/wiki/Philosophy':
    print('Reached Philosophy')
elif no_links == 1:
    print('Reached a page with no links')
else:
    print('Looping through the same articles again')


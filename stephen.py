import urllib2
import requests
from bs4 import BeautifulSoup
import lxml

html = ('https://en.wikipedia.org/wiki/Stephen_Hawking')
content = requests.get(html).content
soup = BeautifulSoup(content,'lxml')
tags = soup.findAll('div',{'class':'toc'})

len(tags)
#print(soup)

tag = soup.find('div',{'class':'toc'})
#print(type(tag))

links = tag.findAll('a')
#print(links)

for link in links:
    #print(link.text)
     results = soup.find_all('span', attrs = {'class':'short_desc'})
#print(results)
#print(html)
#print(soup.title)
#print(soup.title.string)
#print(soup.title.text)
#print(soup.p)

for paragraph in soup.find_all('a'):
    print (paragraph.string)
    for paragraph in soup.find_all('p'):
        print (paragraph.string)
        for paragraph in soup.find_all('p'):
            print (paragraph.text)
    
print(soup.get_text())

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

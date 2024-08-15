from bs4 import BeautifulSoup
import requests
import os

if os.path.exists('input.txt'):
    url, selector, keywords, skip = open('input.txt').read().split('\n')
else:
    url = input('URL: ')
    selector = input('Selector: ')
    keywords = input('Keywords: ')
    skip = input('Skip: ')

print('')

html_doc = requests.get(url).text

soup = BeautifulSoup(html_doc, 'html.parser')
elements = soup.select(selector)

titles = set()

for i, element in enumerate(elements):
    if i % int(skip) != 0:
        continue
    for keyword in keywords.lower().split(' '):
        if keyword in element.text.lower():
            titles.add(element.text.strip())

for title in titles:
    print(title)
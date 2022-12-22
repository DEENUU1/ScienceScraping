import requests
from bs4 import BeautifulSoup
import re

NATURE_URL = 'https://www.nature.com/latest-news'
nature_page = requests.get(NATURE_URL)
nature_soup = BeautifulSoup(nature_page.content, 'html.parser')

nature_headers = nature_soup.find_all('h3', class_='c-article-item__title mb10')

# THis for loop is to get all articles links
# for link in nature_soup.find_all('a'):
#     print(link.get('href'))


# This for loops is to get all headers 
for header in nature_headers:
    print(header.text, end="\n"*2)
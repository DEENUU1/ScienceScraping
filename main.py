import requests
from bs4 import BeautifulSoup
import csv

NATURE_URL = 'https://www.nature.com/nature/articles?type=news'
nature_page = requests.get(NATURE_URL)
nature_soup = BeautifulSoup(nature_page.content, 'html.parser')

nature_link_element = nature_soup.find_all('h3', class_='c-card__title')

print('NATURE NEWS')

def nature_news(nature_link_element):
    for index, header in enumerate(nature_link_element, start=1):
        nature_header_link = header.find('a')
        nature_link = nature_header_link['href']
        nature_header = nature_header_link.text
        print('https://www.nature.com/' + nature_link)
        print(index, nature_header)

print(nature_news(nature_link_element))
print("\n\nAll news are available here: 'https://www.nature.com/latest-news'")
print("I'm still working on displaying links under every article name.")

URANIA_URL = 'https://www.urania.edu.pl/'
urania_page = requests.get(URANIA_URL)
urania_soup = BeautifulSoup(urania_page.content, 'html.parser')

urania_header_h3 = urania_soup.find_all('h3')

print('\n\nURANIA NEWS')

def urania_news(urania_header_h3):
    data = []
    for index, header in enumerate(urania_header_h3, start=1):
        urania_header_link = header.find('a')
        urania_header_span = urania_header_link.find('span')
        text = urania_header_span.text

        data.append({'Text': text,
                     'Link': 'https://www.urania.edu.pl' + urania_header_link['href']})

        print('https://www.urania.edu.pl/' + urania_header_link['href'])
        print(index, text, end='\n' * 1)

    return data



urania_news_data = urania_news(urania_header_h3)
print(urania_news(urania_header_h3))
print("\n\nAll news are available here: 'https://www.urania.edu.pl/'")
print("I'm still working on displaying links under every article name.")


with open('news.csv', 'w', newline='') as csv_file:
    fieldnames = ['Text', 'Link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(urania_news_data)


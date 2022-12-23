import requests
from bs4 import BeautifulSoup
import csv

'''START OF NATURE SCRAPING'''

NATURE_URL = 'https://www.nature.com/nature/articles?type=news'
nature_page = requests.get(NATURE_URL)
nature_soup = BeautifulSoup(nature_page.content, 'html.parser')
nature_link_element = nature_soup.find_all('h3', class_='c-card__title')
print('NATURE NEWS')

def nature_news(nature_link_element):
    nature_data = []
    for index, header in enumerate(nature_link_element, start=1):
        nature_header_link = header.find('a')
        nature_link = nature_header_link['href']
        nature_header = nature_header_link.text

        nature_data.append({'Text': nature_header,
                     'Link': 'https://www.urania.edu.pl' + nature_link})

        print('https://www.nature.com/' + nature_link)
        print(index, nature_header)

    return nature_data

nature_news_data = nature_news(nature_link_element)

'''END OF NATURE SCRAPING'''


'''START OF URANIA SCRAPING'''

URANIA_URL = 'https://www.urania.edu.pl/'
urania_page = requests.get(URANIA_URL)
urania_soup = BeautifulSoup(urania_page.content, 'html.parser')
urania_header_h3 = urania_soup.find_all('h3')
print('\n\nURANIA NEWS')

def urania_news(urania_header_h3):
    urania_data = []
    for index, header in enumerate(urania_header_h3, start=1):
        urania_header_link = header.find('a')
        urania_header_span = urania_header_link.find('span')
        text = urania_header_span.text

        urania_data.append({'Text': text,
                     'Link': 'https://www.urania.edu.pl' + urania_header_link['href']})

        print('https://www.urania.edu.pl/' + urania_header_link['href'])
        print(index, text, end='\n' * 1)

    return urania_data

urania_news_data = urania_news(urania_header_h3)

'''END OF NATURE SCRAPING'''


'''WRITING TO CSV FILE ALL DATA'''

with open('news.csv', 'w', newline='') as csv_file:
    fieldnames = ['Text', 'Link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(urania_news_data)
    writer.writerows(nature_news_data)

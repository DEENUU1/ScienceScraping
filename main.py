import requests
from bs4 import BeautifulSoup
import csv
import xlsxwriter

'''START OF NATURE SCRAPING'''
try:
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

            nature_data.append({'Title': nature_header,
                         'Link': 'https://www.urania.edu.pl' + nature_link})

            print('https://www.nature.com' + nature_link)
            print(index, nature_header)

        return nature_data

    nature_news_data = nature_news(nature_link_element)

except requests.exceptions.ConnectionError:
    print('No internet connection. Please try again')

'''END OF NATURE SCRAPING'''


'''START OF URANIA SCRAPING'''
try:
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

            urania_data.append({'Title': text,
                         'Link': 'https://www.urania.edu.pl' + urania_header_link['href']})

            print('https://www.urania.edu.pl' + urania_header_link['href'])
            print(index, text, end='\n' * 1)

        return urania_data

    urania_news_data = urania_news(urania_header_h3)

except requests.exceptions.ConnectionError:
    print('No internet connection. Please try again')


'''END OF NATURE SCRAPING'''


''' START OF SPACEFLIGHTNOW SCRAPING'''
try:
    SFN_URL = 'https://spaceflightnow.com/'
    sfn_page = requests.get(SFN_URL)
    sfn_soup = BeautifulSoup(sfn_page.content, 'html.parser')
    sfn_header_h3 = sfn_soup.find_all('h3')
    print('\n\nSPACE FLIGHT NOW NEWS')

    def sfn(sfn_header_h3):
        sfn_data = []
        for index, header in enumerate(sfn_header_h3, start=1):
            sfn_header_link = header.find('a')
            sfn_header_title = sfn_header_link.text

            sfn_data.append({'Title': sfn_header_title,
                                'Link': 'https://www.urania.edu.pl' + sfn_header_link['href']})

            print(sfn_header_title)
            print(sfn_header_link['href'])

        return sfn_data

    sfn_news_data = sfn(sfn_header_h3)

except requests.exceptions.ConnectionError:
    print('No internet connection. Please try again')

'''WRITING TO CSV FILE ALL DATA'''

with open('news.csv', 'w', newline='') as csv_file:
    fieldnames = ['Title', 'Link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    try:
        writer.writerows(urania_news_data)
        writer.writerows(nature_news_data)
        writer.writerows(sfn_news_data)
    except NameError:
        print('Something went wrong. Please try again')
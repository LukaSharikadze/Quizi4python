import requests
from bs4 import BeautifulSoup
from time import sleep
import csv


link_opt = {'groups' : 'bottom_250', 'start': 1}
url = 'https://www.imdb.com/search/title/'
lang = {'Accept-Language':'en-US'}

file = open('shedegebi.csv', 'w', newline='\n')
file_a = csv.writer(file)
file_a.writerow(['Title', 'Rating', 'Year', 'Length'])

while link_opt['start']<=201:
    res = requests.get(url, headers=lang, params=link_opt)

    content = res.text

    soup = BeautifulSoup(content, 'html.parser')

    whole = soup.find('div', {'class':'lister-list'})
    movie_list = whole.find_all('div', {'class':'lister-item'})

    for movie in movie_list:
        saxeli = movie.h3.a.text
        div_rating = movie.find('div', {'class':'inline-block ratings-imdb-rating'})
        reitingi = div_rating.strong.text
        div_runtime = movie.find('span', {'class':'runtime'})
        dro = div_runtime.text
        div_year = movie.find('span', {'class':'lister-item-year text-muted unbold'})
        weli = div_year.text.strip('(').strip(')').replace('(', '').replace(')', '')
        file_a.writerow([saxeli, reitingi, weli, dro])
        print(saxeli)
        print(dro)
        print(weli)
        print(reitingi)
    link_opt['start'] += 50
    sleep(15)
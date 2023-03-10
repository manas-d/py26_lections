import csv
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from datetime import datetime


def get_html(url):
    response = requests.get(url)
    return response.text

def get_deps_links(html):
    links = []
    soup = BeautifulSoup(html, 'lxml')
    catalog = soup.find('div', class_='grid-deputs')
    items = catalog.find_all('div', class_='dep-item')
    for item in items:
        a = item.find('a').get('href')
        print(a)
        link = 'http://kenesh.kg' + a
        links.append(link)
    return links


def get_all_links():
    res = []
    for i in range(1, 6):
        url = f'http://kenesh.kg/ru/deputy/list/35?page={i}'
        html = get_html(url)
        dep_links = get_deps_links(html)
        res.extend(dep_links)
    return res

def get_deps_data(link):
    html = get_html(link)
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('div', class_='deput-name').text
    except:
        name = 'Нет имени!'

    info = soup.find('div', class_ ='deput-info').text.strip()
    dep_info = info.split()
    dep_info = ' '.join(info)
    bio = soup.find('div', class_='tab-content').text.strip()
    data = {'name': name, 'info':dep_info, 'bio':bio, 'link': link}
    return data

def prepare_csv():
    with open ('deputaty.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['ФИО', "Информация", "Биография", "Ссылка на страницу"])

def write_to_csv(data):
    with open ('deputaty.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['info'], data['bio'], data['link']])
        print (f'{data["name"]} - parsed!')

def make_all(link):
    data = get_deps_data(link)
    write_to_csv(data)

def main():
    prepare_csv()
    links = get_all_links()
    # for link in links: #последовательно
    #     data = get_deps_data(link)
    #     write_to_csv(data)
    with Pool(20) as pool: #параллельно
        pool.map(make_all, links)

if __name__ == '__main__':
    start = datetime.now()
    main()
    finish = datetime.now()
    print(f'Парсинг занял: {finish - start}')

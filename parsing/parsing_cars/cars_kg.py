from bs4 import BeautifulSoup as bs
import requests
import csv

count = 0

def get_html(url: str) -> str:
    '''Получает html код определенного сайта'''
    response = requests.get(url)
    return response.text

def get_data(html:str) -> list:
    '''Функция парсер, получает все данные с сайта'''
    soup = bs(html, 'lxml')
    catalog = soup.find('div', class_ = 'catalog-list')
    cars = catalog.find_all('a', class_ = 'catalog-list-item')
    result = []
    for car in cars:
            
        name = car.find('span', class_ = 'catalog-item-caption').text.strip()
        try:
            img = car.find('img', class_ = 'catalog-item-cover-img').get('src')
        except:
            img = 'No picture'
        price = car.find('span', class_ = 'catalog-item-price').text
        year = car.find('span', class_ = 'caption-year').text.strip()
        mile = car.find('span', class_ = 'catalog-item-mileage').text.strip()
        desc = car.find('span', class_ = 'catalog-item-descr').text.strip()
        

        data = {
            'name': name,
            'price': price,
            'year': year,
            'mile':mile,
            'desc': desc,
            'img': img
        }

        result.append(data)

    return result

def write_to_csv(data:dict) -> None:
    '''Функция для записи всех данных в CSV файл'''

    with open('carsss.csv', 'a') as file:
        fieldnames = ['#', 'Name', 'Price', 'Year', 'Mile', 'Desc', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        global count

        for car in data:
            count += 1
            writer.writerow ({
                '#': count,
                'Name': car['name'],
                'Price': car['price'],
                'Year':car['year'],
                'Mile': car['mile'],
                'Desc': car['desc'],
                'Image':car['img']
            })

def prepare_csv() -> None:
    '''Функция которая подготовит csv файл'''
    with open ('carsss.csv', 'w') as file:
        fieldnames = ['#', 'Name', 'Price', 'Year', 'Mile', 'Desc', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '#': '#',
            'Name': 'Name',
            'Price': 'Price',
            'Year': 'Year',
            'Mile': 'Mile',
            'Desc': 'Desc',
            'Image':'Image'
            })

def main():
    i = 1
    prepare_csv()
    while True:
        url = f'https://cars.kg/offers/{i}'
        html = get_html(url)
        data = get_data(html)
        write_to_csv(data)
        print(f'Спарсили {i} страницу!')
        if i == 15:
            break
        i += 1
        

main()


import telebot
from telebot import types

token = '5979985933:AAEaf4hhdcX0XL9jo4wgSOeLV4bDkBi8qGc'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    with open ('carsss.csv', 'r') as file:
        bot.send_document(message.chat.id, file)

bot.polling()



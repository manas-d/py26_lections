from bs4 import BeautifulSoup as bs
import requests
import lxml

URL = 'https://www.kivano.kg/'

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html, URL):
    soup = bs(html, 'lxml')
    blog_products = soup.find('div', class_='product_vitrina')
    products = blog_products.find_all('div', class_='product_box')
    list_ = []
    for product in products:
        title = product.find('div', class_='product_title').text
        price = product.find('div', class_='product_price').text.replace('\n','')
        img_div = product.find('div', class_='product_img')
        img = img_div.find('img').get('src')

        list_.append({'Title':title, "Price":price, 'Image':f"{URL}{img.replace('/','',1)}"})

    return list_


html = get_html(URL)

print(get_data(html, URL))


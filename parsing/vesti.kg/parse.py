"""
1)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""

# from bs4 import BeautifulSoup as bs
# import requests
# import csv

# count = 0

# def get_html(url: str) -> str:
#     response = requests.get(url)
#     return response.text

# def get_data(html:str) -> list:
#     soup = bs(html, 'lxml')
#     catalog = soup.find('div', class_ = 'itemListView')
#     result = [] 
#     news = catalog.find_all('div', class_ = 'itemBody')
#     data = {'news': news}
#     result.append(data)
#     return result

# def write_to_csv(data:dict) -> None:
#     with open('news.csv', 'a') as file:
#         fieldnames = ['#', 'news']
#         writer = csv.DictWriter(file, fieldnames)
#         global count

#         for title in data:
#             count += 1
#             writer.writerow ({
#                 '#': count,
#                 'news': title['news'],
#             })

# def prepare_csv() -> None:
#     with open ('news.csv', 'w') as file:
#         fieldnames = ['#', 'news']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow({
#             '#': '#',
#             'news': 'news'
#             })

# def main():
#     i = 1
#     prepare_csv()
#     while True:
#         url = f'https://vesti.kg'
#         html = get_html(url)
#         data = get_data(html)
#         write_to_csv(data)

# main()
'''========================'''
# import requests
# from bs4 import BeautifulSoup
# import csv

# # Запрашиваем HTML-страницу
# url = "https://vesti.kg/"
# response = requests.get(url)

# # Создаем объект BeautifulSoup для парсинга страницы
# soup = BeautifulSoup(response.text, "html.parser")

# # Находим все элементы с названиями новостей
# titles = soup.find_all("h3", class_="post-title")

# # Создаем CSV-файл для записи результатов
# with open("vesti_news.csv", "w", newline="") as csvfile:
#     # Создаем объект writer для записи в CSV-файл
#     writer = csv.writer(csvfile)

#     # Записываем заголовки столбцов в CSV-файл
#     writer.writerow(["Title"])

#     # Записываем названия новостей в CSV-файл
#     for title in titles:
#         writer.writerow([title.text.strip()])


"""
2)	EXTRA: Спарсить https://www.kinopoisk.ru/lists/movies/top250/ и записать результат в csv файл
"""


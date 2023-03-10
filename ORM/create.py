import peewee
from models import Category, Product
import random

def add_category (name):
    try:
        data = Category(name=name.lower().strip())
        data.save()
        print(f'Сохранили категорию {name.strip()}')
    except (peewee.IntegrityError, peewee.InternalError):
        print('Такая категория уже существует')

# add_category('      Платья    ')
# add_category('Джинсы')
# add_category('Футболки')
# add_category('Свитеры')
# add_category('Обувь')

def add_product(name, price, category_name):
    try:
        category_id = Category.get(name=category_name.lower().strip())
    except peewee.DoesNotExist:
        category_id = None

    if category_id:
        data = Product(title = name, price = price, category_id = category_id)
        data.save()
        print(f'Сохранили товар {name}!')
    else:
        print(f'Категории {category_name} не существует!')

# add_product('Zara t-shirt', 300, 'Футболки')
# add_product('Levis', 500, 'Джинсы')
# add_product('Supreme t-shirt', 1000, 'Футболки')
# add_product('DG', 900, 'Платья')
# add_product('Prada', 1100, 'Платья')
# add_product('Tomas Muntz', 700, 'Обувь')
# add_product('Gucci', 400, 'Свитер')




# ------------------------------ Добавление новых данных ------------------------------ #

# add_category ('cars')
# add_category('telefony')

# with open ('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     # print(ls)
#     for x in ls:
#         name = x.replace('\n', '')
#         price = random.randint(5000, 200000)
#         add_product(name, price, 'cars')



# with open('files/telefon.txt', 'r') as file:
#     ls = file.readlines()
#     for x in ls:
#         name = x.replace('\n', '')
#         price = random.randint(200, 1000)
#         add_product(name, price, 'telefony')


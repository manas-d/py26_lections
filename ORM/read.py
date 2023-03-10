import peewee
from models import Product, Category


def get_all_categories():
    return Category.select()

def get_all_products():
    return Product.select()

# categories = get_all_categories()
# # print(categories)
# print('Категории в БД: ')
# for x in categories:
#     # print(type(x))
#     print(x)
#     print(x.name)
#     print(x.created_at)
#     print()

# products = get_all_products()
# print('Все товары в БД: ')
# for x in products:
#     print(x.title, x.price, x.category_id.name)
#     print()

'''вывод продуктов в зависимости от категории'''

# products = get_all_products()
# category = int(input('Введите категорию (1-платья, 2-джинсы, 3-футболки, 4-свитеры, 5-обувь): '))
# for x in products:
#     if x.category_id.category_id == category:
#         print(x.title, x.price, x.category_id.name)

'''вывод данных о продуктах в зависимости от категории'''

category_name = input('Vvedite title categorii: ').lower().strip()
try:
    category = Category.get(name=category_name)
except peewee.DoesNotExist:
    print('Такой категории нет!')
else:
    for product in category.products: # related name
        print(f'Title: {product.title}, price: {product.price}, category: {product.category_id.name}')

'''вывод id категории в зависимости от названия категории'''

# print(category)
# print(category.category_id, type(category.category_id))
# print(category.name, type(category.name))
# print(category.created_at, type(category.created_at))


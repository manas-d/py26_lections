from models import Product, Category

# Команда query.execute() выполняет запрос в таблице

'''Обновление данных'''

# query = Product.update(price=500).where(Product.title == 'Zara t-shirt')
# print(query)
# query.execute()

'''Увеличение цены на все товары'''

# query = Product.update(price=(Product.price + Product.price * 0.5))
# query.execute()

'''Изменение цены на товары 1 и 3 категории'''

# query = Product.update(price=200000).where(Product.category_id == 1 and Product.category_id == 3)
# query.execute()



'''Удаление данных'''
'''Удаление через запрос'''

# query = Product.delete().where(Product.id == 9)
# query.execute()

'''Удаление через объект'''

# product = Product.get(id = 4)
# print(product, product.title)
# product.delete_instance()

'''Удаление через условие'''э

# query = Product.delete().where(Product.id >= 9)
# query.execute() 
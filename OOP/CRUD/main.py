from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin


class Product(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    def save(self):
        import json
        with open ('data.json', 'w') as file:
            json.dump(self.objects, file, indent =4)
        return 'Saved!'
    

smartphones = Product()
print(smartphones.post(title = 'Redmi Note 10', description = 'The best phone for own price!', qty = 10, price = 250))
print(smartphones.post(title = 'Redmi Note 20', description = 'The flagman of Redmi phones!', qty = 5, price = 600))
print(smartphones.post(title = 'Iphone 14 Pro Max', description = 'New phone, cool and best!', qty = 15, price = 1300))
print(smartphones.post(title = 'Samsung S22 Ultra', description = 'The best phone for android lovers!', qty = 8, price = 1000))
print(smartphones.post(title = 'Poco Phone 19', description = 'The poco phone for poco users!', qty = 4, price = 300))

print()
print(smartphones.list()) #создает список/ленту из товаров/постов
print()
print(smartphones.detail(5)) #выводит 5 id 
print(smartphones.detail(15)) #выводит ошибку 404, Not Found, т.к. нет такого id
print()
print(smartphones.patch(5, title = 'Poco Phone 20', price = 500))
print(smartphones.patch(15, title = 'Poco Phone 20'))
print()
print(smartphones.delete(5))
print()
print(smartphones.list())
print(smartphones.save())

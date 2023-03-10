class CRUD:
    __products = []
    __id = 0

    def _get_id(self):
        self.__id += 1
        return self.__id

    def _get_product(self, id):
        for x in self.__products:
            if x['id'] == id: return x
        return False


    def create(self):
        print('CREATE of prodect!')
        title = input('Enter name of product: ')
        price = input('Enter price: ')
        self.__products.append({
            'id': self._get_id(),
            'title': title,
            'price': price
        })
    def list_of_products(self):
        print('All products: ')
        for x in self.__products:
            print(x['title'])

    def detail_product(self):
        print('Detail: ')
        id = int(input('Введите id продукта для функции detail!')) # 565
        product = None
        for x in self.__products:
            if x['id'] == id:
                product = x
        print(product if product else 'Нет такого продукта')

    def update_product(self):
        print('Update')
        id = int(input('Введите id продукта для функции update:'))
        product = self._get_product(id)
        if not product:
            print('Нет такого продукта!')
            return 
        choice = input('Что изменить(title/price):')
        index = self.__products.index(product)
        self.__products[index][choice] = input('Введите новое значение: ')

    def delete_product(self):
        print('DELETE')
        id = int(input('Введите ID продукта для функции Delete:'))
        product = self._get_product(id)
        if not product:
            print('Нет такого продукта')
            return
        self.__products.remove(product)
        print('Удалено!')

product = CRUD()
product.create()
product.create()
product.list_of_products()
# product.detail_product()
# product.detail_product()
# product.update_product()
# product.detail_product()
product.delete_product()
product.list_of_products()
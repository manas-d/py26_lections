# import random

# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Oromo']
# p = 0
# m = 0
# k = 0 
# l = 0
# o = 0
# for x in range(0, 1_000_000):
#     # print(x)
#     choice = random.choice(ls)
#     # print(choice)
#     if choice.lower() == 'plov':
#         p += 1
#     elif choice.lower() == 'manty':
#         m+=1
#     elif choice.lower() == 'kuurdak':
#         k+=1
#     elif choice.lower() == 'lagman':
#         l += 1
#     elif choice.lower() == 'oromo':
#         o += 1
# print('Результаты голодных игр:')
# print(f'Plov: {p}\nManty: {m}\nKuurdak: {k}\nLagman: {l}\nOromo: {o}')

# print(dir(list))
# import json

# def get_sorted(json_filename: str) -> list[dict]:
#     with open (json_filename) as file:
#         res = json.load(file)
#         res.sort(key = lambda x: x['rating'], reverse = True)
#     return res

# print(get_sorted('test.json'))


#JSON 11 task

import json

def update(id: int, title: str=None, price: int=None, rating: float=None) -> None:
    with open('new_db.json', 'r+') as file_:
        python_obj = json.load(file_)
        print(python_obj)
        id_list = []
        for dict_ in python_obj:
            if id == dict_['id']:
                id_list.append(id)
        
        if id not in id_list:
            raise ValueError
        else:
            
            for dict_ in python_obj:
                dict_['title']=title if not None else ...
                dict_['price']=price if not None else ...
                dict_['rating']=rating if not None else ...
                json_obj = json.dumps(dict_)
                file_.write(json_obj)
    

update(1, 'iphone', 1222, 12.0)

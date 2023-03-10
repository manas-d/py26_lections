'''ПРАКТИКА'''

'''Cоздание таблиц:'''

# CREATE TABLE blogger (
#     id serial PRIMARY KEY,
#     name varchar(50));

# CREATE TABLE post (
#     id serial primary key,
#     owner_id int REFERENCES blogger (id),
#     body text,
#     created_at DATE);

'''Заполнение данных:'''

# INSERT INTO blogger(name) VALUES ('John'), ('Sultan Katana'), ('Jamie');

# INSERT INTO post(owner_id, body, created_at) VALUES
#     (1, 'My first blog post! Hello world!', '2023.02.24'),
#     (1, 'today is a good day!', '2023.01.01'),
#     (1, 'It is my bad-bad day!', '2023.02.24');

# INSERT INTO post(owner_id, body, created_at) VALUES
#     (3, 'Lanister always pays his debts!', '2023.02.24'),
#     (3, 'I will be back!', '2023.01.01');

# INSERT INTO post(owner_id, body, created_at) VALUES
#     (2, 'I am hungry', '2023.02.24');

'''--------------------------------------------------------------------------'''

'''SHOP'''

'''Cоздание таблиц:'''

# CREATE TABLE customer (
#     id serial PRIMARY KEY,
#     name varchar(50));

# CREATE TABLE product (
#     id serial PRIMARY KEY,
#     title varchar (50),
#     price decimal);

# CREATE TABLE cart (
#     id serial PRIMARY KEY,
#     customer_id int REFERENCES customer(id),
#     product_id int REFERENCES product(id)
# );

'''Заполнение данных:'''

# INSERT INTO customer (name) VALUES ('Sultan'), ('John'), ('Jamie');

# INSERT INTO product (title, price) VALUES (
#     ('KKS', 340),
#     ('Iphone 14', 70000),
#     ('Potato', 200),
#     ('Ananas', 470),
#     ('Icecream', 120)
# );

# INSERT INTO cart (customer_id, product_id) VALUES
#     (1,1), (1,1), (1,1), (1,3), (1,3),
#     (2,2), (2,2),
#     (3,4),(3,5);

'''--------------------------------------------------------------------------'''

'''АГРЕГАТНЫЕ ФУНКЦИИ'''

# SUM -  функция, которая считывает сумму всех записей в сгруппированном поле

#пример из SHOP

# SELECT c.name, SUM(p.price) AS tolal_price
# FROM product AS p JOIN cart ON p.id = cart.product_id JOIN customer AS c ON c.id = cart.customer_id GROUP BY c.name;

'''ARRAY_AGG - объединяет записи с группированного поля в массив'''

# SELECT b.name, ARRAY_AGG(post.body) FROM blogger as b
    # JOIN post ON b.id = post.owner_id
    # GROUP BY b.name;


'''--------------------------------------------------------------------------'''

'''SHAKESPEARE'''

# 1. Вытащить все произведения в которых sourse = Moby и кол-во параграфов меньше 100:
# SELECT title, source, totalparagraphs FROM work WHERE source = 'Moby' AND totalparagraphs < 100;

# 2. Найти кол-вл глав в каждом произведении:
# SELECT COUNT(*), work.title FROM chapter JOIN work ON work.workid = chapter.workid GROUP BY work.title ORDER BY COUNT(*) DESC

# 3. Найти сколько произведений относится к каждому жанру:
# SELECT COUNT(*), genretype FROM work GROUP BY genretype ORDER BY count;

# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений:
# SELECT title, totalparagraphs FROM work;

# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания
# SELECT ch.charname, ch.speechcount, work.title, work.genretype, work.year
# FROM character_work AS ch_w
# JOIN character AS ch ON ch_w.charid = ch.charid
# JOIN work ON ch_w.workid = work.workid
# WHERE ch.speechcount > 200 ORDER BY work.year;

# ----
# Ошибка
# SELECT ch.charname, MAX(ch.speechcount), ARRAY_AGG (work.title) FROM character_work AS ch_w
# JOIN character AS ch ON ch_w.charid = ch.charid
# JOIN work ON ch_w.workid = work.workid
# WHERE ch.speechcount > 200 ORDER BY MAX(ch.speechcount) DESC LIMIT 10;

# 6. Вытащить героя, который чаще всех появляется в произведениях
# SELECT ch.charname, COUNT(*) AS works_count
# FROM character_work AS ch_w
# JOIN character AS ch ON ch.charid = ch_w.charid
# GROUP BY ch.charname ORDER BY works_count DESC LIMIT 1;
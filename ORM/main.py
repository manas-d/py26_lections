'''ORM (object relational mapping)''' 
# ORM - объектно реляционное программирование - технология программирования, благодаря которой разработчики могут использовать язык программирования для взаимодействия с реляционной базой данных (PostgreSQL, MySQL). Вместо того, чтобы писать сырые запросы на операторах SQL, вы будете писать код ООП на языке программирования. Это очень сильно ускоряет разработку приложения и БД, особенно на начальных этапах.

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database = 'orm_db',
    user = 'manas',
    password = '1212',
    host = 'localhost',
    port = 5432
)

# db.connect()
from peewee import *

# Создаем базу данных для пользователей
users_db = SqliteDatabase("users.db")
quotes_db = SqliteDatabase("quotes.db")


# Создаем базовую модель БД с цитатами
class QuoteBaseModel(Model):
    index = PrimaryKeyField(unique=True)

    class Meta:
        database = quotes_db
        order_by = "index"


# Создаем базовую модель БД с пользователями
class UserBaseModel(Model):
    index = PrimaryKeyField(unique=True)

    class Meta:
        database = users_db
        order_by = "index"


# Создаем таблицу с пользователями
class User(UserBaseModel):
    nickname = CharField()
    points = IntegerField(default=0)

    class Meta:
        db_table = "users"


# Создаем таблицу с цитатами
class Quote(QuoteBaseModel):
    film_title = CharField()
    film_quotes = TextField()

    class Meta:
        db_table = "quotes"

from peewee import *
import os

# Создаем базу данных для пользователей
users_db = SqliteDatabase("users.db")
quotes_db = SqliteDatabase("quotes.db")


class QuoteBaseModel(Model):
    index = PrimaryKeyField(unique=True)

    class Meta:
        database = quotes_db
        order_by = "index"


class UserBaseModel(Model):
    index = PrimaryKeyField(unique=True)

    class Meta:
        database = users_db
        order_by = "index"


class User(UserBaseModel):
    nickname = CharField()
    points = IntegerField(default=0)

    class Meta:
        db_table = "users"


class Quote(QuoteBaseModel):
    film_title = CharField()
    film_quotes = TextField()

    class Meta:
        db_table = "quotes"

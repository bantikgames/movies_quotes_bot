from models import *

# Создание базы данных пользователей и цитат
if __name__ == "__main__":
    with users_db:
        users_db.create_tables([User], safe=True)
    with quotes_db:
        quotes_db.create_tables([Quote], safe=True)

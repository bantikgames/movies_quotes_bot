from models import *
import json

# Шаблон для создания JSON-файла
question_data = {"Questions": []}


# Генерируем 10 вопросов с цитатами и сохраняем их в JSON
async def generate_question_json():
    for num_of_quest in range(0, 11):
        random_quote = Quote.select().order_by(fn.Random()).limit(4)
        question_data["Questions"].append(
            {
                "Number": num_of_quest,
                "Question": [{
                    "Quote": [obj.film_quotes for obj in random_quote],
                    "Film": [obj.film_title for obj in random_quote],
                }]

            }
        )
    with open("question.json", "w+") as json_file:
        json.dump(question_data, json_file, indent=2)
    print("GENERATE COMPLETE")


# Очищаем JSON-файл с цитатами
async def clear_question_json():
    with open("question.json", "w+") as json_file:
        json_file.truncate()
    print("CLEAR COMPLETE")


# Формируем один вопрос с цитатаой и 4-мя вариантами ответа
def get_question(question_number):
    with open("question.json", "r") as jsonfile:
        data = json.load(jsonfile)
        quote = data["Questions"][question_number]["Question"][0]["Quote"][0]
        film = data["Questions"][question_number]["Question"][0]["Film"][0]

    return quote, film

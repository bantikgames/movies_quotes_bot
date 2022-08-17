from models import *
import json

question_data = {"Questions": []}


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


async def clear_question_json():
    with open("question.json", "w+") as json_file:
        json_file.truncate()
    print("CLEAR COMPLETE")


def get_question(question_number):
    with open("question.json", "r") as jsonfile:
        data = json.load(jsonfile)
        quote = data["Questions"][question_number]["Question"][0]["Quote"][0]
        film = data["Questions"][question_number]["Question"][0]["Film"][0]

    return quote, film
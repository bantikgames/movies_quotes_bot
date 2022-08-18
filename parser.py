from bs4 import BeautifulSoup
from models import *
import requests

# Задаем URLы для сбора данных и список классов для обработки
urls = ["https://citaty.info/movie", "https://citaty.info/series"]
classes = ["taxonomy-term vocabulary-vocabulary-4", "taxonomy-term vocabulary-vocabulary-25"]

# Парсим содержимое страниц и сохраняем это все в БД с цитатами
for url in urls:
    for html_class in classes:
        r = requests.get(url)
        parser = BeautifulSoup(r.text, "lxml")
        parser_result = parser.findAll("div", class_=html_class)
        for result in parser_result:
            result_name = result.find("div", class_="term-content-wrapper").find("div", class_="term-content").find(
                "div", class_="term-name "
                              "field-type-entityreference")
            result_url = result_name.find("a", href=True)
            result_quotes_count = result.find("div", class_="term-teaser-meta").find("div",
                                                                                     class_="term-quotes-count").text
            quotes_list_request = requests.get(result_url["href"])
            quotes_parser = BeautifulSoup(quotes_list_request.text, "lxml")
            quotes_result = quotes_parser.findAll("div", class_="field field-name-body field-type-text-with-summary "
                                                                "field-label-hidden")
            for quotes in quotes_result:
                quote = quotes.find("div", class_="field-items").find("div", class_="field-item even last").find(
                    "p").text
                Quote.create(film_title=result_name.string.split(" (")[0], film_quotes=quote)

print("All done")
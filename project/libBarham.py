import requests
import json


def process(book:dict):
    book_name , book_category = book.values()
    if book_category == 'math':
        url = "http://127.0.0.1:8000/math/"
    elif book_category == 'physic':
        url = "http://127.0.0.1:8000/physic/"
    elif book_category == 'chess':
        url = "http://127.0.0.1:8000/chess/"

    res = requests.get(url)
    data = res.json()
    for item in data:
        if book_name == item['name']:
            return "bad query"

    requests.post(url=url, data=book)
    
'''
import requests
import json


def process(book):
    urls = dict(math='http://127.0.0.1:8000/math/', physic='http://127.0.0.1:8000/physic/', chess='http://127.0.0.1:8000/chess/')
    data = requests.get(urls[book['category']]).json()
    for i in range(len(data)):
        if data[i]['name'] == book['name']:
            return 'bad query'
    requests.post(urls[book['category']], data=book)
 
'''
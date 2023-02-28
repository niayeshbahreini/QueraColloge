import requests

def process(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            return 'I can\'t recognize it'
        if all(data[0]['category'] == i['category'] for i in data):
            return data[0]['category']
        else:
            return 'I can\'t recognize it'
    else:
        return 'Bad Query'
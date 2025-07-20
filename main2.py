#Задание 2: Параметры запроса
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.
import requests
import pprint

params = {'userId': 1}
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url, params=params)
response_json = response.json()
pprint.pprint(response.status_code)
pprint.pprint(response_json)
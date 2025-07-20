# Задание 3: Отправка данных
# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа.
# В поле для ответа загрузи скриншоты сделанных заданий или ссылку на Git.
import requests
import pprint

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.post(url, data=data)
response_json = response.json()
pprint.pprint(response.status_code)
pprint.pprint(response_json)
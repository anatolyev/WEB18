from requests import post


print(post('http://localhost:8080/api/news', json={}).json())

print(post('http://localhost:8080/api/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:8080/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())
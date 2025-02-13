import requests


map_request = "https://static-maps.yandex.ru/v1?ll=37.677751,55.757718&spn=0.016457,0.00619&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
response = requests.get(map_request)
print(response)

# Запишем полученное изображение в файл.
map_file = "map1.png"
with open(map_file, "wb") as file:
    file.write(response.content)
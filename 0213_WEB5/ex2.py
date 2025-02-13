
import requests
api_server = "https://static-maps.yandex.ru/v1"

lon = "37.677751"
lat = "55.757718"
delta1 = "0.016457"
delta2 = "0.00619"
apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta1, delta2]),
    "apikey": apikey,
}
response = requests.get(api_server, params=params)

print(response)

# Запишем полученное изображение в файл.
map_file = "map2.png"
with open(map_file, "wb") as file:
    file.write(response.content)
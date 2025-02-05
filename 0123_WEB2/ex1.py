import requests
import json

geo_request = "https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Магадан&format=json"
response = requests.get(geo_request)

if response:
    print(response, type(response))
    print(response.content)
    json_response = response.json()
    print(json_response)
    with open("ex1.json", "w", encoding="utf8") as json_file:
        json.dump(json_response, json_file, ensure_ascii=False)
else:
    print("Ошибка запроса")
    print(geo_request)
    print("HTTP статус",
          response.status_code, "(",
          response.reason, ")")

toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][1]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
print(toponym)
import json

with open("ex1.json", encoding="utf8") as f:
    data = json.load(f)

print(data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["AdministrativeArea"]["SubAdministrativeArea"]["SubAdministrativeAreaName"])
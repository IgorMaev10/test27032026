import json
import requests
import csv

# 11
url = 'http://api.open-notify.org/astros.json'
params = {
    'limit': 0,
    'skip': 0
}

response = requests.get(url=url, params=params)
response_json = response.json()

with open("people.json", mode="w", encoding='utf-8') as json_file:
    json.dump(response_json, json_file, indent=4, ensure_ascii=False)

# 12
with open(r'C:\Users\user\Downloads\airport-codes_csv.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        if 'UA' in row['iso_country']:
            print(row['name'])


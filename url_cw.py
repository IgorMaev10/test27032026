import requests

url = 'https://dummyjson.com/recipes'
params = {
    'limit': 0,
    'skip': 0
}
response = requests.get(url=url, params=params)
response_json = response.json()

recipes = response_json['recipes']

dish = "pizza"
tag = "Italian"
temperature = "190°C"

dish_recipes = []
tagged_recipes_quantity = 0
most_calories = 0
most_calorie_dish = []
recipes_by_temperature = []
review_quantity = 0

for recipe in recipes:
    if dish in recipe['name'].lower():
        dish_recipes.append(recipe)

    if tag in recipe['tags']:
        tagged_recipes_quantity += 1

    if recipe["caloriesPerServing"] > most_calories:
        most_calories = recipe['caloriesPerServing']
        most_calorie_dish = recipe

    if temperature in recipe['instructions'][0]:
        recipes_by_temperature.append(recipe)

    review_quantity += recipe['reviewCount']
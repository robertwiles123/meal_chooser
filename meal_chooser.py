import random

meal_option = {
    'Spag Bol': 'No book',
    'Chili': 'No book',
    'Leek cabanara': 'No book',
    'Curry': 'No book',
    'Jumbalia': 'Pinch of nom',
}

while True:
    meal_amount = input('How many meals would you like chosen for you? ')
    try:
        meal_amount = int(meal_amount)
        keys = list(meal_option.keys())
        try:
            selected_meals = random.sample(keys, meal_amount)
            break
        except ValueError:
            length_meals = len(meal_option)
            print(f"Too many options chosen, max number of meals {length_meals}")
    except ValueError:
        print("Not a number, ,must be a number! ")

keys = list(meal_option.keys())



i = 1
for key in selected_meals:
    value = meal_option[key]
    print(f"Meal {i} is {key}. The book is {value}")
    i = i + 1
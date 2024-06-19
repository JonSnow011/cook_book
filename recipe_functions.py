def get_recipe(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients = []
            num_of_ingredients = int(file.readline().strip())
            for _ in range(num_of_ingredients):
                ingredient, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({'ingredient_name': ingredient, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = ingredients
            file.readline()  # Пропускаем пустую строку между блюдами
    return cook_book

def main():
    file_name = 'recipes.txt'  # Предположим, что ваши данные находятся в файле recipes.txt
    cook_book = get_recipe(file_name)
    for dish, ingredients in cook_book.items():
        print(dish)
        for ingredient in ingredients:
            print(ingredient)

if __name__ == "__main__":
    main()
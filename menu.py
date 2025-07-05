breakfast_menu = {
    "Pancakes": 5000,
    "Omelette": 7000,
    "Tea": 2000
}

lunch_menu = {
    "Chicken Stew": 10000,
    "Beef Curry": 12000,
    "Vegetable Salad": 8000
}

def display_menu(menu_name, menu_items):
    print(f"\n{menu_name} Menu:")
    print("-" * 20)
    for item, price in menu_items.items():
        print(f"{item}: {price} UGX")

display_menu("Breakfast", breakfast_menu)


display_menu("Lunch", lunch_menu)
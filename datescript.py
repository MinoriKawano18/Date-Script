#!/usr/bin/env python3

# Create a python script that displays a date simulator
# Allow the user to input who is on the date with them
# User inputs their budget for the date
# Script prints the restraurant menu 
# User inputs their item choices from the menu for themselves and their date
# Script tells the user how much money is left within the budget 
# At the end of the date, the use must agree to pay the bill and the final budget is shown

# Restaurant menu

menu = {
        "Wings": {"Course": "Appetizer", "Ingredients": ["chicken", "garlic", "BBQ Sauce"], "Price": 15, "Description": "These are the best wings in the world!"},
        "Steak and Eggs": {"Course": "Main", "Ingredients": ["Wagyu", "Eggs", "Salt and Pepper"], "Price": 45, "Description": "High grade Wagyu with Free range organic eggs from Japan"},
        "Sushirito": {"Course": "Main", "Ingredients": ["Salmon", "Rice", "Nori"], "Price": 25, "Description": "Freshly imported salmon from coldest Japanese oceans"},
        "Kakigori": {"Course": "Dessert", "Ingredients": ["Shaved Ice", "Condensed Milk", "Strawberry"], "Price": 10, "Description": "Refreshing dessert"},
}

def print_menu(menu):
    print("\nRestaurant Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

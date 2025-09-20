#concession program in python

menu = {"Kuku": 30.25,
        "Beaf": 25.10,
        "Mutton": 15.00,
        "Chips": 10.12,
        "Pizza": 30.00,
        "Ugali": 50.00,
        "Tea": 15.20,
        "Coffee": 10.50,
        "Juice": 50.35,
        "Popcorn": 5.25,
        "Soda": 25.20,
        "Bread": 50.30 }
cart = []
total = 0

print("          MENU          ")
for key, value in menu.items():
    print(f"{key:10}: $.{value:.2f}")
print("                     ")

while True:
    food = input("Select an Item from the menu, (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print(cart)
print("                     ")
print("        YOUR ORDER         ")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print( )
print(f"your total is $.{total:.2f}")




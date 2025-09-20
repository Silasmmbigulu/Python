#course cart program in python

languages = []
prices = []
total = 0

while True:
    language = input("Enter a language you wish to study (q to quit): ")
    if language.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price to study {language} : $."))
        languages.append(language)
        prices.append(price)

print("                  ")
print("                  ")
print("-------YOUR CART---------")
for language in languages:
    print(language)

print("             ")
for price in prices:
    total += price

print(f"Your total price is $.{total}")

#while loop with not logical operator

language = input("Enter programming language you like(x to quit): ")

while not language =="x":
    print(f"You like {language} programming language")
    language = input("Enter another programming language you like(x to quit): ")

print("byee, nice time")

#while loop plus or logical operator

num = int(input("Enter a number between 1-20: "))

while num < 1 or num > 20:
    print(f"{num} is not valid!")
    num = int(input("Enter a number between 1-20: "))

print(f"your number is {num }")
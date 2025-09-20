#python program prompting the user to enter his/her age and that it shud not be less than zero

age = int(input("Enter your age: "))

while age < 0:
    print("age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")

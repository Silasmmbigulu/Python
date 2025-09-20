#while loop executes codes while a certain condition remains true
#python program prompting a user to enter his/her name

name = input("Enter your name: ")

while name == "":
    print("You did not enter any name. Please enter a name")
    name = input("Enter your name: ")

print(f"Hello {name }")
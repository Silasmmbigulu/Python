# python weight converter

weight = float (input("Enter your weight: "))
unit = input("Kilograms or Pounds (Kgs or L): ")

# weight conversion

if unit == "Kgs":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"your weight is: {round (weight, 4)} {unit}.")
else:
    print(f"the unit '{unit}' is invalid!")


#Lenghth converter

lenghth = float(input("Enter the lenghth: "))
unit = input("Kilometers or Meters (Km or M ): ")

#conversion operation

if unit == "M":
    lenghth = lenghth / 1000
    unit = "Km."
elif unit == "Km":
    lenghth = lenghth * 1000
    unit = "M."
    print(f"The lenghth is: {round(lenghth, 4)} {unit}.")
else:
    print(f"the unit {unit} is not valid!")

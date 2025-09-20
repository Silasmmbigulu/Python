#pyhon compound interest calculator

principal = 0
rate = 0
time = 0

principal = float(input("Enter the Pricipal amount: "))
while principal <= 0:
    print("Pricipal can't be zero or less than zero")
    principal = float(input("Enter the Pricipal amount: "))

rate = int(input("Enter the interest rate: "))
while rate <= 0:
    print("Rate can't be zero or less than zero")
    rate = int(input("Enter the interest rate: "))

time = int(input("Enter time in year/s: "))
while time <= 0:
    print("Time can't be zero or less than zero")
    time = int(input("Enter time in year/s: "))

print("-------------------")
print(f"The principal amount is $ {principal}")
print(f"The interest rate is {rate}%")
print(f"The time is {time} years")
print("------------------")

total = principal * pow((1 + rate/100), time)
print(f"Balance after {time} year/s is: $ {total:.2f}")

    
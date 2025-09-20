#python calculator
operator = input("Enter an operetor (+,-,* or /): ")
num1 = float (input("Enter the first number: "))
num2 = float (input("Enter the second number: "))

#performing the arithmetic
if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
     result = num1 * num2
     print(round(result, 3))
elif operator == "/":
     result = num1 / num2
     print(round(result, 3))
else:
     print(f"the operator ({operator}) is invalid ! ")
    


#program to calculate electricity bill of a customer
#prompt the user for inputs
Customer_ID = int(input("Enter Custmer ID: "))
Customer_Name = str(input("Enter Customer Name: "))
Units_Consumed = int(input("Enter Units Consumed: "))

#determing total bill
if Units_Consumed <= 199:
    charge_per_unit = 1.20
elif Units_Consumed < 400:
    charge_per_unit = 1.50
elif Units_Consumed < 600:
    charge_per_unit = 1.80
else:
    charge_per_unit = 2.00

#calculationc
Total_Bill = Units_Consumed * charge_per_unit
print(f"The total bill is: {Total_Bill}")

surcharge_fee = 0.15

#calculating the surcharged fee
if Total_Bill > 400:
    surcharge_fee = Total_Bill * 0.15 
    Total_Bill+=surcharge_fee
    print(f"The new total bill after surcharged is: {Total_Bill}")

#Ensuring the minimun bill is Ksh.100
if Total_Bill < 100:
   Total_Bill = 100
   print(f"The total amount to be paid is: {Total_Bill}")

print("--------------------.")
print(f"Customer Name is: {Customer_Name}")
print(f"Customer ID is: {Customer_ID}")
print(f"Units consumed is: {Units_Consumed }")
print(f"Charge per unit is: {charge_per_unit}")
print(f"The total bill is: {Total_Bill}")
print(f"Surcharge fee is: {surcharge_fee}")
print(f"Total amount to be paid is: {Total_Bill }")

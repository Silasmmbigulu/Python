#python program to calculate gross pay, taxes and net pay for workers

#user inputs
name = str(input("Enter your full Names: "))
employer_id = int(input("Enter your work ID: "))
hours_worked = int(input("Enter hours worked: "))
hourly_wage = float(input("Enter your hourly wage: "))

#calculating overtime charges
#working hours = 8 hrs, above that it's overtime
#incase of overtime, 150% bonus
if hours_worked > 8:
    overtime = (hours_worked - 8)
    print(f"Your Overtime hours are {overtime}")
    gross_pay = ((8 * hourly_wage) + (overtime * hourly_wage * 1.5))
    print(f"Your gross pay for today is $.{gross_pay}")
else:
    gross_pay = (hours_worked * hourly_wage)
    print(f"No overtime, so your Gross pay is $.{gross_pay}")

#calculating taxes
#if workers gross pay is <= 600, the tax is 15%
#else, tax is 15% * 600 plus 20% on gross pay minus the 600
if gross_pay <= 600:
    tax = gross_pay * 0.15
    print(f"Your Tax is $.{tax}")
else:
    tax = ((600 * 0.15) + ((gross_pay - 600) * 0.20))
    print(f"Your tax is $.{tax}")

#calculating workers net pay per day
net_pay = (gross_pay - tax)
print(f"your net pay for today is $.{net_pay}")

#worker's net salary
#if the woker does what he does daily therefore his/her income per month will be:
monthly_salary = (net_pay * 30)

#displaying the output
print("        ")
print("-----------")
print(f"Name: {name}")
print(f"work ID: {employer_id}")
print(f"Your Gross Pay is $.{gross_pay}")
print(f"Your Taxes are $.{tax}")
print(f"Your net pay per day is $.{net_pay}")
print("        ")
print("       ------        ")
print(f"Hello {name} of ID {employer_id} it's been a month now and you've maintained your daily routine.")
print(f"So your monthly income is $.{monthly_salary:.2f}")
print("Have a nice day!!")

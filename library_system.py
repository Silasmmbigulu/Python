#library management system
book_id = int(input("Enter the Book ID:"))
due_date = int(input("Enter Due date: "))
return_date = int(input("Enter Return date: "))

#days overdue
days_overdue = (return_date - due_date)
print(f"Days Overdue = {days_overdue}")

#getting fine amount
if days_overdue <= 7:
    fine_rate = 20
elif days_overdue <= 14:
    fine_rate = 50
else:
    fine_rate = 100
 
print(f"The Fine Rate = {fine_rate}")

#calculating fine amount
fine_amount = (fine_rate * days_overdue)
print(f"The Fine Amount is $ {fine_amount}.")

#Display the output
print("--------------------")
print(f"Book ID is {book_id}")
print(f"The Due Date is {due_date}")
print(f"The Return date is {return_date}")
print(f"Days Overdue are {days_overdue}")
print(f"The Fine Rate is $.{fine_rate}")
print(f"The Fine Amount is $.{fine_amount}")
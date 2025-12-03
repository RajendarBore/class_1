
acno = input("Enter Account Number: ")
name = input("Enter Name: ")
current_balance = float(input("Enter Current Balance: "))
amount = float(input("Enter Transaction Amount: "))
code = input("Enter Transaction Code (d/w): ")


if code == 'd' or code == 'D':
    net_balance = current_balance + amount
elif code == 'w' or code == 'W':
    net_balance = current_balance - amount
else:
    print("Invalid transaction code!")
    exit()


print("\n----- Account Details -----")
print("Account Number:", acno)
print("Customer Name:", name)
print("Previous Balance:", current_balance)
print("Transaction Amount:", amount)
print("Transaction Code:", code)
print("Net Balance:", net_balance)
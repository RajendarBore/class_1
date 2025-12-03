employeeno=input("enter employee number")
employeename=input("enter the name")
employeesalary=float(input("enter the salary"))
designation=(input("enter the disignation"))

if designation=="m":
    bonus=0.20*employeesalary
elif designation=="a":
    bonus=0.10*employeesalary
elif designation=="r":
    bonus=0.05*employeesalary
else:
    print("invalid disignation")
    bonus=0
print("\n--- Employee Salary Details ---")
print("Employee Number:", employeeno)
print("Employee Name:", employeename)
print("Basic Salary:", employeesalary)
print("Bonus:", bonus)
print("Total Salary:",employeesalary)



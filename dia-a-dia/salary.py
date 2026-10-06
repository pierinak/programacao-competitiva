name = input()
salary = float (input())
sold = float (input())
percentage = 15

totalSalary = salary + (sold * (percentage/100))

print (f"TOTAL = R$ {totalSalary:.2f}")
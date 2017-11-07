nome = input()
fixed_salary = float(input())
made_sales = float(input())
commission = (made_sales*(15/100))
total = fixed_salary+commission

print("TOTAL = R$ %.2f"%total)
monthly_income = input("Enter your monthly income: ")

monthly_expenses = input("Enter your total  monthly expenses: ")

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings is ${monthly_savings}.") 

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is ${projected_savings}.")

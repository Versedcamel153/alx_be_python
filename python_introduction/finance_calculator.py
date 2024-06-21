print("Enter your monthly income:")
monthly_income = input()
print("Enter your total  monthly expenses:")
total_monthly_expenses = input()

monthly_savings = int(monthly_income) - int(total_monthly_expenses)
print(f"Your monthly savings is ${monthly_savings}.") 

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is ${projected_savings}.")

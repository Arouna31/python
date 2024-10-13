# Recalculating the repayment schedule for the new loan parameters

# Given values for the recalculation:
P = 3472.49  # Principal amount
annual_rate = 18.04 / 100  # 18.04% nominal annual interest rate
n = 12  # 6-month repayment period

# Monthly interest rate
r = annual_rate / 12

# Applying the formula for monthly payment
M = P * (r * (1 + r)**n) / ((1 + r)**n - 1)

# Initialize variables
balance = P
schedule = []

# Create the repayment schedule for 6 months
for month in range(1, n + 1):
    interest = balance * r  # Interest for the month
    principal_payment = M - interest  # Principal portion of the payment
    balance -= principal_payment  # Remaining balance after payment
    schedule.append([f"Month {month}", round(M, 2), round(interest, 2), round(principal_payment, 2), round(balance, 2)])

# Create a DataFrame for better visualization
print(principal_payment)

# Mathematical Operations in Python
# DataTypes
# Converting types

from art import LOGO
print(LOGO)
print("\nWelcome to the tip calculator!!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 20, or 15? "))
split = int(input("How many people to split the bill? "))
tip_amount = (tip / 100) * bill

# Calculate the total amount (bill + tip)
total_bill = bill + tip_amount

# Calculate how much each person should pay
total = total_bill / split

print(f"Each person shoul pay : ${total:.2f}")

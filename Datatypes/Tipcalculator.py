
#if the bill was $150 split between 5 people, with 12% tip.
#Each person should pay (150.00/5)*1.12

print("Welcome to th tip calculator $")
total_bill = float(input(("What was the total bill?")))
tip = float(input(("What percentage tip would you like to give? $")))
people = int(input(("How many people to split the bill?")))

bill_with_tip = (total_bill/people)*(1+tip/100)

bill_with_tip_afterFormate = "{:.2f}".format(bill_with_tip)

print(f"Each person should pay ${bill_with_tip_afterFormate}")


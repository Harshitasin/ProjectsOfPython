#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("************************  Tip Calculator  ************************************")
print("Welcome to tip calculator")
bill=int(input("What was the total bill?"))
tip=int(input("What percentage tip would you like to give? %"))
people=int(input("How many people to split the bill?"))
pay=round(((bill/people)*(1+(tip/100))),2)
print("Each person should pay: $",+pay)
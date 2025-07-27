#QUESTION 1:

distance = float(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest you ride a bicycle to your destination.")
elif distance < 300:
    print("I suggest you ride a motorcycle to your destination.")
else:
    print("I suggest you drive a supercar to your destination.")


#QUESTION 2:


rate = 0.51

daily = rate * 24
weekly = daily * 7
monthly = daily * 30

funds = 918
days_possible = funds / daily
print("1. Cost for 1 day: $", round(daily, 2))
print("2. Cost for 1 week: $", round(weekly, 2))
print("3. Cost for 1 month: $", round(monthly, 2))
print("4. Days you can run with $918:", int(days_possible))


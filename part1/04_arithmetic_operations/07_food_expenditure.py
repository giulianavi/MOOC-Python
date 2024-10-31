times_week = float(input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of a typical student lunch"))
groceries_spent = float(input("How much money do you spend on groceries in a week?"))

daily = float((times_week * lunch_price + groceries_spent) / 7)

weekly = daily * 7


print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")
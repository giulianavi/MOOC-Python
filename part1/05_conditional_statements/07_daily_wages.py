hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")

sunday = hourly_wage * hours_worked * 2
daily = hourly_wage * hours_worked

if day != 'Sunday':
    print(f"Daily wages: {daily} euros")
if day == 'Sunday':
    print(f"Daily wages: {sunday} euros")
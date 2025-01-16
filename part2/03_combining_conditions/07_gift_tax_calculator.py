value = int(input("Value of gift: "))

if value < 25000:
    low = 5000
    base = 100
    rate = 0.08
elif value < 55000:
    low = 25000
    base = 1700
    rate = 0.10
elif value < 200000:
    low = 55000
    base = 4700
    rate = 0.12
elif value < 1000000:
    low = 200000
    base = 22100
    rate = 0.15
else:
    low = 1000000
    base = 142100
    rate = 0.17

if value < 5000:
    result = 0
else:
    result = base + (value - low) * rate

if result == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {result} euros")
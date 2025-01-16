year = int(input("Year: "))
next_leap = year + 1

while True:
    if next_leap % 4 == 0 and next_leap % 100 != 0 or next_leap % 400 == 0:
        break
    next_leap += 1 
print(f"The next leap year after {year} is {next_leap}")
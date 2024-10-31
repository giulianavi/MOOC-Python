name = input("Write your name: ")
if name != "Jerry":
    portions = float(input("How many for the portions?"))
    then = portions * 5.90
    print(f"The total cost is {then}\nNext please!")
elif name == "Jerry":
    print("Next please!")
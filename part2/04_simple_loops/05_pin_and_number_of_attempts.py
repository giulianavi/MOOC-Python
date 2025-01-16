attempt = 0
correct = 4321

while True:
    pin = int(input("PIN: "))
    if pin != correct:
        print("Wrong")
        attempt += 1
    elif attempt == 0:
        print("Correct! It only took you one single attempt!")
        break
    if pin == correct and attempt > 0:
        attempt += 1
        print(f"Correct! It took you {attempt} attempts")    
        break
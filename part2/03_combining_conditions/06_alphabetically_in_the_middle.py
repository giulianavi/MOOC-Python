letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

middle_letter = letter2

if letter1 < letter2 and letter1 < letter3:
    if letter2 > letter3:
        middle_letter = letter3
elif letter1 > letter2 and letter1 > letter3:
    if letter2 < letter3:
        middle_letter = letter3
elif letter1 > letter2:
    if letter1 >= letter3:
        middle_letter = letter3
    else: 
        middle_letter = letter1
else:
     middle_letter = letter1


print(f"The letter in the middle is {middle_letter}")
# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

import random
digits = list(range(10))
random.shuffle(digits)
code = digits[:3]
print(code)
count = 0

while True:
    clues = []
    guess = [int(x) for x in str(input("What is your guess? "))]
    count += 1
    if(guess == code):
        print("Correct! You guessed the number in", count, "tries")
        break
    for i in range(0, len(guess)):
        if(guess[i] == code[i]):
            clues.append("MATCH")
        elif(guess[i] in code):
            clues.append("CLOSE")

    if(clues == []):
        print("Nope")
    else:
        for clue in clues:
            print(clue)

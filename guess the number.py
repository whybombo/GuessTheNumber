import random
myNum = random.randint(0,9)

print("Try to guess a Number 0 - 9 that im thinking of...")

while True:

    userNum = int(input("What is your guess? : "))

    if (myNum == userNum):
        print("Yes that is the number!")
        break
    
    elif ( myNum > userNum) :
        print("too low, try again", end="\n\n")
    
    else:
        print("too high, try again", end="\n\n")
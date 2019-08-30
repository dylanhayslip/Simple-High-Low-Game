from random import randrange

rn = (randrange(1, 10))
rnTwo = (randrange(1, 10))
finRn = abs(rn - rnTwo)
hhr = "higher" or "Higher"
lwr = "lower" or "Lower"
hh = "high" or "High"
ll = "low" or "Low"

userAns = input("Would you like a number? ")
if userAns == "yes":
    userHl = input("Will the next number be higher or lower than " + str(rn) + "? ")
else: exit()

if rn > rnTwo and userHl == hhr:
    print("The number was " + str(rnTwo) + "! You lost! ")
elif rn > rnTwo and userHl == hh:
    print("The number was " + str(rnTwo) + "! You lost! ")
elif rn < rnTwo and userHl == hhr:
    print("You are correct! the number was " + str(rnTwo) + "! ")
elif rn < rnTwo and userHl == hh:
    print("You are correct! the number was " + str(rnTwo) + "! ")
elif rn < rnTwo and userHl == lwr:
        print("The number was " + str(rnTwo) + "! You lost! ") 
elif rn < rnTwo and userHl == ll:
        print("The number was " + str(rnTwo) + "! You lost! ") 
elif rn > rnTwo and userHl == lwr:
        print("You are correct! the number was " + str(rnTwo) + "! ")
elif rn > rnTwo and userHl == ll:
        print("You are correct! the number was " + str(rnTwo) + "! ")
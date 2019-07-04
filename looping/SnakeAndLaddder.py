import random as r
userChoice=0
systemChoice=0
SH=65
ST=30
LH=85
LT=35
userOneCurrentLocation=0
userTwoCurrentLocation=0

def findUserCurrentLocation(userInput,userCurrentLocation):
    if (userInput+userCurrentLocation)==LT:
        print("Ohh thats great you took ladder Congrats !!!")
        return LH
    elif (userInput+userCurrentLocation)==SH:
        print("you have been bit by snake")
        return ST
    else:
        return userCurrentLocation+userInput

while True:
    while True:
        userChoice=int(input("Enter your value of dice :"))
        if userChoice>=1 and userChoice <=6:
            break
        else:
            print("Dice value should only between 1 to 6 ")
    print(f"User one input is {userChoice}")
    userChoice=findUserCurrentLocation(userChoice,userOneCurrentLocation)
    userOneCurrentLocation=userChoice
    if userOneCurrentLocation >=100:
        print("User one win")
        break
    else:
        print(f"User one at postion{userOneCurrentLocation}")
    systemChoice=r.randint(1,6)
    print(f"system input is {systemChoice}")
    systemChoice=findUserCurrentLocation(systemChoice,userTwoCurrentLocation)
    userTwoCurrentLocation=systemChoice
    if userTwoCurrentLocation>=100:
        print("System won")
        break

    else:
        print(f"System at postion {userTwoCurrentLocation}")




import random as r
user_choice=0
system_choice=0
SH=45
ST=25
LH=85
LT=27
user_one_current_location=0
user_two_current_location=0

def find_user_current_location(user_input, user_current_location):
    if (user_input + user_current_location)==LT:
        print("Ohh thats great you took ladder Congrats !!!")
        return LH
    elif (user_input + user_current_location)==SH:
        print("you have been bit by snake")
        return ST
    else:
        return user_current_location + user_input

while True:
    while True:
        user_choice=int(input("Enter your value of dice :"))
        if 1 <= user_choice <= 6: # userChoice >=1 and userChoice <= 6
            break
        else:
            print("Dice value should only between 1 to 6 ")
    print(f"User input is {user_choice}")
    user_choice=find_user_current_location(user_choice, user_one_current_location)
    user_one_current_location=user_choice
    if user_one_current_location >=100:
        print("User win")
        break
    else:
        print(f"User position at {user_one_current_location} ")
    system_choice=r.randint(1, 6)
    print(f"System input is {system_choice}")
    system_choice=find_user_current_location(system_choice, user_two_current_location)
    user_two_current_location=system_choice
    if user_two_current_location>=100:
        print("System won")
        break

    else:
        print(f"System position at {user_two_current_location}")




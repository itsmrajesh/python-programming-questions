def greet_user(name='user'):
    print("Hello",name)

greet_user()
greet_user("Rajesh")

def pos_args(name='user',age=18,loc='India'): #positional parameter
    print("Welcome",name)
    print(age)
    print(loc)

pos_args("rajesh")
pos_args(age=21,name='Lakshman')
pos_args("John",loc='USA')

def sqrt_num(n,num=None): #n is required parameter , num is positional parameter
    if num is not None:
        print(num**2)
    else:
        print("Square of number is num**2")

sqrt_num(0,12)


def sign_up(first_name,last_name):
    print(f"Welcome {first_name} {last_name}")


sign_up(last_name='Rajesh',first_name='M') #key word agruments

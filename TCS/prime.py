import math as m
def is_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True


def foo(n):
    if is_prime(n):
        val = m.sqrt(n)
        print(round(val,2))


foo(int(input()))

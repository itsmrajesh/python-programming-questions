import math as m

"""1 2 3 3 5 5 7 7 7 7 11 11 13 13 13 13 17 17"""
def is_prime(n):
    if n <= 1:
        return False
    else:
        val = round(m.sqrt(n))
        for i in range(2, val + 1):
            if n % i == 0:
                return False
        return True

a=1
p=2

def get_next_prime(p):
    p += 1
    while True:
        if is_prime(p):
            return p
        else:
            p += 1

num=int(input())
print("1",end=" ")
for i in range(1,num//2):
    next_prime=get_next_prime(p)
    r=next_prime-p
    for i in range(r):
        print(p,end=" ")
    p=next_prime


import math as m

"""print these series 1 2 1 3 5 3 7 5 11 8"""
def is_prime(n):
    if n <= 1:
        return False
    else:
        val = round(m.sqrt(n))
        for i in range(2, val + 1):
            if n % i == 0:
                return False
        return True


num = int(input())
a = 1
b = 0
p = 2
for i in range(num // 2 + 1):
    print(a, end=" ")
    sum = a + b
    b = a
    a = sum
    if i == num // 2:
        break
    while True:
        if is_prime(p):
            print(p, end=" ")
            p += 1
            break
        else:
            p += 1
print()
'''if num % 2 == 0:
    print(f"{num} term is {a}")
else:
    print(f"{num} term is {p}")'''

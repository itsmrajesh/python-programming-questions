import math as m


def is_prime(n):
    if n <= 1:
        return False
    else:
        val = round(m.sqrt(n))
        for i in range(2, val + 1):
            if n % i == 0:
                return False
        return True


def foo(n):
    if is_prime(n):
        val = m.sqrt(n)
        print(round(val, 2))
    else:
        print("0.00")


foo(int(input()))

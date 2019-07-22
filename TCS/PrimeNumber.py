import math as m
def is_prime(n):
    n = int(n)
    if n == 1:
        return False
    else:
        val = round(m.sqrt(n))
        if n % 2 == 0:
            for i in range(2, val):
                if n % i == 0:
                    return False
        else:
            for i in range(3, val, 2):
                if n % i == 0:
                    return False
        return True


print(is_prime(input()))

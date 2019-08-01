import math as m


def get_binary_to_decimal(num):
    decimal, i = 0, 0
    while num > 0:
        rem = num % 10
        decimal += rem * m.pow(2, i)
        i += 1
        num //= 10
    return round(decimal)


num=int(input())
print(get_binary_to_decimal(num))

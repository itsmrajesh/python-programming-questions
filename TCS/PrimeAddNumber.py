import math as m


def is_prime(n):
    #n=int(n)
    if n <= 1:
        return False
    else:
        val = round(m.sqrt(n))
        for i in range(2, val+1):
            if n % i == 0:
                return False

        return True


def get_sum(num):
    sum=0
    for i in num:
        sum += int(i)

    return sum

num=input()
print(is_prime(get_sum(num)))
if len(num)<=1:
    print("Invalid")
else:
    print(is_prime(get_sum(num[1::2])))

print(is_prime(get_sum(num[::2])))



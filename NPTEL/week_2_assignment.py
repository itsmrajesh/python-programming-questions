import math as m


def intreverse(n):
    n = str(n)
    rev = n[::-1]
    return int(rev)  # for -ve cases


def is_prime(n):
    if n <= 1:
        return False
    else:
        val = round(m.sqrt(n))

        for i in range(2, val + 1):
            if n % i == 0:
                return False

        return True


def sumprimes(lst):
    s = 0
    for i in lst:
        if is_prime(i):
            s += i
    return s


def matched(s):
    c = 0
    for ele in s:
        if ele == '(':
            c += 1
        elif ele == ')' and c < 0:
            return False
        elif ele == ')' and c >= 0:
            c -= 1

    return c == 0


print(intreverse(242789))
print(matched("zb%78"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))
print(matched("a)*(?"))
print(sumprimes([3, 3, 1, 13]))
print(sumprimes([-3, 1, 6]))

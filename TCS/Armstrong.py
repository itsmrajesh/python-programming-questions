def is_armstrong(n):
    s = str(n)
    lst = list(s)
    sum = 0
    for i in lst:
        sum += pow(int(i), len(lst))

    return sum == n


print(is_armstrong(int(input())))

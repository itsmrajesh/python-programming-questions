def reverse(n):
    n = str(n)
    lst = list(n)
    lst.reverse()
    s = ''
    for ele in lst:
        s += ele

    return int(s)


print(reverse(input()))

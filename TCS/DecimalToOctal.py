def convert_to_octal(n):
    lst = []
    while n != 0:
        lst.append(n % 8)
        n //= 8
    lst.reverse()
    res=''
    for i in lst:
        res +=str(i)
    return int(res)

print(convert_to_octal(int(input())))

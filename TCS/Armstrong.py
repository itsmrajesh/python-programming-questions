def is_armstrong(n):
    s = str(n)
    lst = list(s)
    sum = 0
    for i in lst:
        sum += pow(int(i), len(lst))

    return sum == n


num1 = int(input())
num2 = int(input())
if num1 > 0 and num2 >= num1:
    while num1 < num2:
        if is_armstrong(num1):
            print(num1)
        num1 += 1

else:
    print("Invalid Boundraies")

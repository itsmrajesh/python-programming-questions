"""If the sum of factorial of the digits in any number is equal the given number then the number is called as STRONG number."""
""" Ex = 1! + 4! +5!= 1+24+120 = 145 """


def get_factorial(num):
    if num <= 0:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact


num = input()
sum = 0
for n in num:
    sum += get_factorial(int(n))

print(sum == int(num))

a = int(input())  # 10
b = int(input())  # 20
a, b = b, a
print(a, b)
a = a + b  # a=30
b = a - b  # b=30-20 ,b is swapped
a = a - b  # a= 30-10 , a is swapped
print(a, b)

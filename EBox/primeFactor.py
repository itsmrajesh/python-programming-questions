from prime import is_prime

p=2
num = int(input())
print(help(is_prime(7)))
for i in range(2,num+1):
    if is_prime(i):
        if num%i==0:
            print(i)



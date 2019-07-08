import time
t0=time.time()
limit = int(input("Enter a number :"))
num1=0
num2=1
for i in range(limit+1):
    print(num1)
    next=num1+num2
    num1=num2
    num2=next

t1=time.time()

print(f"Total time taken {t1-t0}")

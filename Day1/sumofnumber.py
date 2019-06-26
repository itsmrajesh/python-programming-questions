num = int(input("Enter a number :"))
numCopy=num
sum=0
while num>0:
    reminder = num%10
    sum += reminder
    num //= 10

print(f"The sum of {numCopy} is {sum}")

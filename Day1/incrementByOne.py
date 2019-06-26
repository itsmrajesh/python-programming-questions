from Day1 import revANumber as r

num = int(input("Enter a number :"))
numCopy=num
rev=0
while num>0:
    reminder = num % 10
    if reminder == 9:
        reminder =0
    else:
        reminder += 1

    rev = rev*10+reminder
    num //= 10

rev =r.revNumber(rev)

print(f"The result of {numCopy} is {rev}")

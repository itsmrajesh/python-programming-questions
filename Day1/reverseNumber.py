num = int(input("Enter a numeber : "))
numCopy=num
rev=0
while num>0:
    rem = num%10
    rev = (rev*10)+rem
    num //= 10

print(f"The rev of {numCopy} is {rev}")

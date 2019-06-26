def isPrime(n):
    if n <2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%2==0:
                return False
        return True


num = int(input("Enter a number to check prime or not :"))

print(f"{num} Prime number" if isPrime(num) else "{num} Not prime Number")

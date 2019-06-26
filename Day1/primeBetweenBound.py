from Day1.primenumber import isPrime
lb = int(input("Enter lower bound :"))
ub = int(input("Enter upper bound :"))

while lb<ub:
    if isPrime(lb):
        print(lb)
        lb += 1
    else:
        lb += 1

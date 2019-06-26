m = int(input("Enter  m value :"))
n= int(input("Enter  n value :"))

#pre defined  print(pow(m,n))

pow=1;
for i in range(1,n+1):
    pow = pow*m

print(f"Power of {m}^{n} is {pow}")

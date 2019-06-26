num = int(input("Enter a Number :"))
su_m=0
for i in range(1,num+1):
    print(f"1/{i}" + " + ",end="")
    su_m += (1/i)

print(f"\nTheir sum is {su_m}")

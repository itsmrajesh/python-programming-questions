n=int(input())
spaces=n*2-2

for i in range(n):
    for space in range(spaces):
        print(end=" ")

    spaces -= 1
    for _ in range(i+1):
        print("*",end=" ")

    print()

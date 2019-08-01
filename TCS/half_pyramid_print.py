n = int(input())

""" Prints pyramid for given number from user """
for i in range(1, n + 1):
    for i in range(1, i + 1):
        print("*", end="")
    print()  # printing next line

print("Inverted below ")
for i in range(n, 0,-1):
    for i in range(1, i + 1):
        print("*", end="")
    print()

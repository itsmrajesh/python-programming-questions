s = input()
size = len(s)
sum = 0
c = 2
for i in range(0, size):
    print(s[i], end=" ")
    sum += int(s[i])
    k = c
    for j in range(size - c+1):
        print(s[j:k], end=" ")
        sum += int(s[j:k])
        k += 1
    c += 1
print()
print(sum)
s=str(sum)
s=s[::-1]
print(int(s))

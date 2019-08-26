"""
Given String s = 1234
possible substrings of "1234" are 1,2,3,4,12,23,34,123,234 and 1234
Sum S = 1+2+3+4+12+23+34+123+234+1234=1670
Reverse R = 761
"""


s = input()
size = len(s)
sum = 0
c = 2
print("All possible combinations of substrings")
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
print("Sum:",sum)
s=str(sum)[::-1] #reverse the string
print("Sum Reverse:",int(s))

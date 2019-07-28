""" problem statement https://ibb.co/9HKYJth """


def rotate_to_left(str, r):
    first = str[0:r]
    last = str[r:]
    return (last + first)


def rotate_to_right(str, r):
    first = str[len(str) - r:]
    last = str[:len(str) - r]
    return (first + last)


def is_anagram(mainstr, sub):
    return sub in mainstr


copy_maintstr = input()
mainstr = copy_maintstr
sub = ""
str_len = len(copy_maintstr)
n = int(input())
for i in range(n):
    rotate = list(map(str, input().split()))
    r = int(rotate[1])
    if r > str_len:
        r = r % str_len
    if rotate[0].upper() == 'L':
        mainstr = rotate_to_left(mainstr, r)

    elif rotate[0].upper() == 'R':
        mainstr = rotate_to_right(mainstr, r)
    print(mainstr)
    sub += mainstr[0]

print(is_anagram(copy_maintstr, sub))
print(sub)

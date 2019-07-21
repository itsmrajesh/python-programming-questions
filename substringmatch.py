def is_match(str, n):
    print(str)
    lst = []
    for i in range(n):
        ss = input()
        lst.append(ss)
    is_matched = False
    for i in range(n):
        for j in range(i + 1, n):
            if sorted(lst[i] + lst[j]) == sorted(str):
                print(lst[i],lst[j])
                is_matched = True

    if not is_matched:
        print("Not Matched")


str = input()
n = int(input())
is_match(str, n)

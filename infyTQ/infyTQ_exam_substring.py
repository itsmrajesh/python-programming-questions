''' Problem Statement https://www.geeksforgeeks.org/infosys-certification-exam-infytq/ '''

''' ex : input: abcabcbb      output :- abc
    ex : input: abcabcdedadcb output :- abcde  
'''


def is_sub(s):
    if len(s) >= 3:
        for word in s:
            if (s.count(word) > 1):
                return False
        return True
    else:
        return False


def get_substring(s):
    l = len(s)
    min = 3
    max = 0
    lst = list()
    for i in range(0, l):
        for j in range(i + 3, l + 1):
            sub = s[i:j]
            # print(sub)
            if is_sub(sub):
                if len(sub) > max:
                    # print(sub)
                    max = len(sub)
                    lst.append(sub)
    if lst == []:
        return -1
    else:
        return lst[-1]


s = input()
print(get_substring(s))
# st = set(s)
# if len(st) > 1:
#     print(get_substring(s))
# else:
#     print(st.pop())

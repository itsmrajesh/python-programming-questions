longest=0

def is_sub(s):
    if len(s)>=3:
        for word in s:
            if (s.count(word)>1):
                return False

        longest=len(s)
        return True
    else:
        return False

def get_substring(s):
    l=len(s)
    min=3
    max=0
    res="-1"
    for i in range(0,l):
        for j in range(i+3,l-3):
            sub=s[i:j]
            if is_sub(sub):
                if len(sub)>max:
                    max=len(sub)
                    res=sub
    return res






s=input()
print(get_substring(s))

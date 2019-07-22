def group_anagrams(lst):
    dct=dict()
    for ele in lst:
        s = ''.join(sorted(ele))
        if dct.get(s):
            dct[s].append(ele)
        else:
            dct[s] = [ele]

    #for k,v in dct.items():
        #print(k)
        #print(v)
    return dct.values()

lst=["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(lst))

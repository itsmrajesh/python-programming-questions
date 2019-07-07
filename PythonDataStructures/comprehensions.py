sentences="Hey how are you "
words="Hey bro you are cool !!!"
lst=[l for l in sentences.split(" ")]
s={ele for ele in lst} #set 1
ss={w for w in words.split()} # set2
print(s)
print(ss)
for ele in s:
    if ele in ss:
        print("ok")
    else:
        print("no")

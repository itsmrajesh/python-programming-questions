vowels="aeiou"
vowels=set(vowels)
data='quintessential'
lst=list(data)
pre = lambda x:x in vowels

print(list(filter(pre,lst)))

identifiers="break case continue default defer else for func goto if map range retuen struct type var"

lst=list(identifiers.split())

word = input()
if word in lst:
    print(f"{word} is keyword")
else:
    print(f"{word} is not a key word")

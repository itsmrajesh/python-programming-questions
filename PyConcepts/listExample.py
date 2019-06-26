import random as r

names = ["rajesh","gokul","sujith","mrudulla"]
for name in names: #processing each elements in list
    print(name)

#add random numbers to it

lst =[r.randint(1,99) for i in range(1,11)]
print(lst)

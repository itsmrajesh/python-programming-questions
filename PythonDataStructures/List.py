name='Rajesh Chowdary'
#convert name to list
name = list(name)
#print(name)
#sliceing
#print(name[::2])
str = "".join(name[:6:])
#print(str)
#join list to one more list
name.extend(list('CSE'))
#print(name)
list1=list("abcdef")
list2=list1 #both are pointing to same address
print(list1)
print(f'List 1{list1}')
print(f'List 2{list2}')
list1.pop()
print("pop element in list1")
print(f'List 1{list1}')
print(f'List 2{list2}')
#it is good practice to copy from one list to another is use list2 = list1.copy()
list2 = list1.copy()
print("After copying list1 to list2")
print(f'Copied List 2= {list2}')
print(f'List 1= {list1}')
list1.pop()
print(f'Afer pop of List 1{list1}')
print(f'After pop of list 1 -> Copied List 2 : {list2}')


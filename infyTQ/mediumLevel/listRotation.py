# Python program to right rotate
# a list by n using list slicing
n = 3

list_1 = [1, 2, 3, 4, 5, 6]
print(list_1[3:6])
print(list_1[0:3])
print("Now combine both")
print(list_1[3:6],list_1[0:3])
list_1 = (list_1[len(list_1) - n:len(list_1)]
				+ list_1[0:len(list_1) - n])
print("Final output ")
print(list_1)

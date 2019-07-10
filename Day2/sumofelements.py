from functools import reduce

lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]


add=lambda x,y:x+y

sum_of_list = reduce(add,lst)
print(sum_of_list)




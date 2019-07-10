from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

iseven = lambda x:x%2==0

filtered_list=list(filter(iseven,lst))

print(filtered_list)

get_squares=lambda x,y:x**2+y**2

sum_of_squares=reduce(get_squares,filtered_list)

print(sum_of_squares)

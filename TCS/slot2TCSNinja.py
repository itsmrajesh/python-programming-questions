arr = input()
arr=list(arr)
arr_len = len(arr)
even_sum, odd_sum = 0, 0
for i in range(arr_len):
    if i % 2 == 0:
        odd_sum += int(arr[i])
    else:
        even_sum += int(arr[i])

print(abs(even_sum-odd_sum))

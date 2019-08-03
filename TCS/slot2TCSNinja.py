arr = list(map(int, input().split()))

arr_len = len(arr)
even_sum, odd_sum = 0, 0
for i in range(arr_len):
    if i % 2 == 0:
        odd_sum += arr[i]
    else:
        even_sum += arr[i]

print(odd_sum, even_sum)

def get_kth_element(arr, k):
    """Returns kth largest element in array or list """
    if k > len(arr):
        return -1
    else:
        return arr[len(arr) - k - 1]


arr = list(map(int, input().split()))
k = int(input())
arr.sort()
ele = get_kth_element(arr, k)
print(ele)

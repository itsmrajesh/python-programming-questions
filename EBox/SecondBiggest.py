def get_second_largest(nums):
    """return second biggest number """
    return sorted(list(nums))[len(nums)-2]

nums=set(map(int,input().split()))
print(get_second_largest(nums))

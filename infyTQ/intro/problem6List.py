#PF-Prac-6
def list123(nums):
    res=False
    for i in range(len(nums)-2):
        if 1 is nums[i] and 2 is nums[i+1] and 3 is nums[i+2]:
            res=True

    return res

nums=[1,1,2,3,4,5]
print(list123(nums))

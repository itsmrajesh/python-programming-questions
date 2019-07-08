# PF-Prac-4
def find_nine(nums):
    # Remove pass and write your code here
    if 9 in nums[:4]:
        return True
    else:
        return False


nums = [1, 0, 4, 9, 6,9]
print(find_nine(nums))

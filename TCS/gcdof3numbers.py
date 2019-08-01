"""GCD of 2 or more numbers Ex:- gcd of 2 4 6 8 16 is 2 """


def get_gcd(a, b):
    if a == 0:
        return b
    else:
        return get_gcd(b % a, a)


nums = list(map(int, input().split()))
res = nums[0]
for n in nums:
    res = get_gcd(n, res)

print(res)

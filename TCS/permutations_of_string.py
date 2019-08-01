from itertools import permutations

data = input()

all_permutations = ["".join(ele) for ele in permutations(data)]

print(all_permutations)



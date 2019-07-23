def get_no_pairs(ids, k):
    size = len(ids)
    pair_count = 0
    for i in range(size):
        for j in range(i + 1, size):
            if abs(ids[i] - ids[j]) == k:
                pair_count += 1
    return pair_count


n = int(input())
ids = []
for i in range(n):
    ids.append(int(input()))
k = int(input())
print(get_no_pairs(ids, k))

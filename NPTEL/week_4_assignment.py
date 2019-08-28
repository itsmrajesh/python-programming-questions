def frequency(l):
    # print(l)
    unique_l = list(set(l))
    # print(unique_l)
    freq_list = [l.count(x) for x in unique_l]
    # print(freq_list)
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    return min_freq_list, max_freq_list


print(frequency([13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14, 7]))


def onehop(lst):
    data = lst
    data.sort(key=lambda tup: tup[0])  # Sorting all tuples in ascending order via first element
    ans = []  # Creating a blank List
    for ele in lst:  # Looping through all elements
        x, y = ele  # Storing Tuple value in x and y
        for ele1 in lst:  # For finding next hop for all destinations
            if ele != ele1:  # To check if it's not the same element in loop
                xx, yy = ele1  # Storing another tuple's value in xx, yy
                if y == xx and x != yy and (x, yy) not in ans:  # checking conditions for adding to ans.
                    # y == xx to check if second element of first tuple is equal to first element of second tuple.
                    # Only then Next Hop is possible
                    # x != y, so that we don't get tuples like (2,2), (3,3) etc.
                    # (x,yy) not in ans, is to ensure that one next hope isn't repeated twice.
                    ans.append((x, yy))  # Adding tuple to ans if all conditions satisfied.
    ans = sorted(ans, key=lambda tup: (
    tup[0], tup[1]))  # Sorting all tuples in ascending order via first element and second element.
    # ans.sort(key=lambda tup: tup[0])
    return ans


print(onehop([(1,3),(1,2),(2,3),(2,1),(3,2),(3,1)]))

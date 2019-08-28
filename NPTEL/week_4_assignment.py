def frequency(l):
    print(l)
    unique_l = list(set(l))
    print(unique_l)
    freq_list = [l.count(x) for x in unique_l]
    print(freq_list)
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    return min_freq_list, max_freq_list


print(frequency([13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14, 7]))

""" Write a program to print all the LEADERS in the array.
An element is leader if it is greater than all the elements to its right side.
And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2},
leaders are 17, 5 and 2 """


def get_leaders(arr):
    leaders_lst = []
    arr_len = len(arr)
    leader = arr[arr_len - 1]
    leaders_lst.append(leader)
    for i in range(arr_len - 2, -1, -1):
        if arr[i] > leader:
            leader = arr[i]
            leaders_lst.append(leader)
    leaders_lst.reverse()
    return leaders_lst


arr = list(map(int, input().split()))
leaders_lst = get_leaders(arr)
print(leaders_lst)

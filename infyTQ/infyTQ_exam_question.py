""" 4, 2, 7, 5, 3, 8, 10, 11, 19 """
""" 2, 3, 5, 8 and 3, 8, 11, 19  """

def get(arr):
    size=len(arr)
    l=list()
    for i in range(size):
        k=arr[i]
        for j in range(i+1,size):
            if k + arr[j] in arr:
                l.append(k)
                l.append(arr[j])
                return l

def get_seq(arr):
    arr.sort()
    lst=list()
    a=get(arr)
    status=True
    if a[0] !=0 and a[1] !=0:
        for i in range(4):
            lst.append(a[0])
            s = a[0]+a[1]
            a[0]=a[1]
            a[1]=s

        for ele in lst:
            if ele not in arr:
                status = False
                break
        if status:
            print(lst)
        else:
            print("-1")

    else:
        print("-1")

lst = list(map(int, input().split()))

get_seq(lst)

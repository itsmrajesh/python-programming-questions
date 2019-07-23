def sort_files(files):
    size=len(files)
    lst=[]
    zero_lst=[]
    for i in files:
        if i=='0':
            zero_lst.append("0")
        else:
            lst.append(i)

    lst.extend(zero_lst)
    for i in lst:
        print(i)





file_nos = list(map(str, input().split()))
sort_files(file_nos)

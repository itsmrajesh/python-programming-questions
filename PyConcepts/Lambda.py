x=lambda x:x**3

lst=[x(i) for i in range(10)]
print(lst)

def get_square(n):
    return lambda x : x**n


n=get_square(2)
print(n(4))

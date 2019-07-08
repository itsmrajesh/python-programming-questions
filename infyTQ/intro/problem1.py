# PF-Prac-1
def add_string(str1):
    if len(str1) < 3:
        return str1
    elif str1.endswith("ing"):
        str1=str1+"ly"
        return str1
    else:
        str1=str1+"ing"
        return str1

str1 = "com"
print(add_string(str1))

# PF-Prac-10
def string_both_ends(input_string):
    if len(input_string) < 2:
        return -1

    else:
        res=""
        res=input_string[0:2]+input_string[-2::]
        return res


input_string = "w3resource"
print(string_both_ends(input_string))

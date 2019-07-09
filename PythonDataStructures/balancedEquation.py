class Stack:

    def __init__(self):
        self.__lst = []

    def push(self, ele):
        self.__lst.append(ele)

    def pop(self):
        return self.__lst.pop()

    def is_empty(self):
        return len(self.__lst) == 0

    def get_stack(self):
        return self.__lst


def match(p1, p2):
    if p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    else:
        return False


def is_balanced(data):
    s = Stack()
    is_bal = True
    index = 0
    while index < len(data) and is_bal:
        ele = data[index]
        if ele in "[({":
            s.push(ele)
        else:
            if s.is_empty():
                return False
            else:
                top = s.pop()
                if not match(top, ele):
                    return False

        index += 1

    if s.is_empty() and is_bal:
        return True
    else:
        return False


input_str = "[[]][{]}"
print(is_balanced(input_str))

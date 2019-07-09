class Stack:

    def __init__(self):
        self.__lst=[]

    def push(self,ele):
        self.__lst.append(ele)

    def pop(self):
        return self.__lst.pop()

    def is_empty(self):
        return len(self.__lst) == 0


    def get_stack(self):
        return self.__lst








class Student:

    def __init__(self, name, usn, sem,marks):
        self.name=name
        self.usn=usn
        self.sem=sem
        self.marks=marks

    def display(self):
        print(self.name)
        print(self.sem)
        print(self.usn)
        print(self.marks)

s1=Student("Rajesh","1NC16CS057",7,8.5)
print(s1.marks)


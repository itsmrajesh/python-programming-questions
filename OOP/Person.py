class Person:
    def __init__(self,name):
        self.name=name


    def talk(self):
        print(f"{self.name} is talking")


p = Person("Rajesh")
p.talk()

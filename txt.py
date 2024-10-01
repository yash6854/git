class Person:
    def __init__(self,name,college):
        self.name = name
        self.college = college

        def show(self):
            print("This is Parent Class")

class Degree(Person):
    def __init__(self,name,college,id):
        super().__init__(name,college)
        self.id = id

        def show1(self):
            print("This is a child Class")
class toppers(Person):
    def __init__(self,name,college,rank):
        super().__init__(name,college)
        self.rank = rank

        def show2(self):
            print("This the child class")
    
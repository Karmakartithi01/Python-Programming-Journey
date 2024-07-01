class Base:
    def __init__(self, num1):
        self.num1 = num1

class Parent1(Base):
    def __init__(self, num1, num2):
        Base.__init__(self, num1)
        self.num2 = num2

class Parent2(Base):
    def __init__(self, num1, num3):
        Base.__init__(self, num1)
        self.num3 = num3

class Child(Parent1, Parent2):
    def __init__(self, num1, num2, num3, num4):
        Parent1.__init__(self, num1, num2)
        Parent2.__init__(self, num1, num3)
        self.num4 = num4
        
    def s(self):
        return self.num1 + self.num2 + self.num3 + self.num4

# End-to-end implementation
child = Child(10,20,30,40)
print(child.s())
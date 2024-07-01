class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        #super().__init__(name)
        self.age = age

    def show(self):
        print(f"Child Name: {self.name}, Age: {self.age}")

# End-to-end implementation
child = Child("Alice", 20)
child.display()  # Parent Name: Alice
child.show()     # Child Name: Alice, Age: 20

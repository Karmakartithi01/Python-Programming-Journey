class Parent:
    def __init__(self, parent_name):
        self.parent_name = parent_name

    def parent_display(self):
        print(f"Parent Name: {self.parent_name}")

class Child1(Parent):
    def __init__(self, parent_name, child1_name):
        super().__init__(parent_name)
        self.child1_name = child1_name

    def child1_display(self):
        print(f"Child1 Name: {self.child1_name}")

class Child2(Parent):
    def __init__(self, parent_name, child2_name):
        super().__init__(parent_name)
        self.child2_name = child2_name

    def child2_display(self):
        print(f"Child2 Name: {self.child2_name}")

# End-to-end implementation
child1 = Child1("John", "Alice")
child2 = Child2("John", "Bob")
child1.parent_display()  # Parent Name: John
child1.child1_display()  # Child1 Name: Alice
child2.parent_display()  # Parent Name: John
child2.child2_display()  # Child2 Name: Bob

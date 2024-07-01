class Grandparent:
    def __init__(self, grandparent_name):
        self.grandparent_name = grandparent_name

    def grandparent_display(self):
        print(f"Grandparent Name: {self.grandparent_name}")

class Parent(Grandparent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)
        self.parent_name = parent_name

    def parent_display(self):
        print(f"Parent Name: {self.parent_name}")

class Child(Parent):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)
        self.child_name = child_name

    def child_display(self):
        print(f"Child Name: {self.child_name}")

# End-to-end implementation
child = Child("Tom", "John", "Alice")
child.grandparent_display()  # Grandparent Name: Tom
child.parent_display()       # Parent Name: John
child.child_display()        # Child Name: Alice

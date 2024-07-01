class Base:
    def __init__(self, base_name):
        self.base_name = base_name

    def base_display(self):
        print(f"Base Name: {self.base_name}")

class Parent1(Base):
    def __init__(self, base_name, parent1_name):
        super().__init__(base_name)
        self.parent1_name = parent1_name

    def parent1_display(self):
        print(f"Parent1 Name: {self.parent1_name}")

class Parent2(Base):
    def __init__(self, base_name, parent2_name):
        super().__init__(base_name)
        self.parent2_name = parent2_name

    def parent2_display(self):
        print(f"Parent2 Name: {self.parent2_name}")

class Child(Parent1, Parent2):
    def __init__(self, base_name, parent1_name, parent2_name, child_name):
        Parent1.__init__(self, base_name, parent1_name)
        Parent2.__init__(self, base_name, parent2_name)
        self.child_name = child_name

    def child_display(self):
        print(f"Child Name: {self.child_name}")

# End-to-end implementation
child = Child("Grandparent", "Parent1", "Parent2", "Alice")
child.base_display()    # Base Name: Grandparent
child.parent1_display() # Parent1 Name: Parent1
child.parent2_display() # Parent2 Name: Parent2
child.child_display()   # Child Name: Alice

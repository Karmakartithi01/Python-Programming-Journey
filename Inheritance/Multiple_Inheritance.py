class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def father_display(self):
        print(f"Father Name: {self.father_name}")

class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def mother_display(self):
        print(f"Mother Name: {self.mother_name}")

class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def child_display(self):
        print(f"Child Name: {self.child_name}")

# End-to-end implementation
child = Child("John", "Jane", "Alice")
child.father_display()  # Father Name: John
child.mother_display()  # Mother Name: Jane
child.child_display()   # Child Name: Alice

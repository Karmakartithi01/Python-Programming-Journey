"""
Single Inheritance

class A1:
    def __init__(self, n1):
        self.N1 = n1
    def show(self):
        return self.N1

class B1(A1):
    def __init__(self, n1,n2):
        super().__init__(n1)
        self.N2 = n2
    def s(self):
        return self.N1 * self.N2
    
single_inheritance = B1(10,2)
value = single_inheritance.s()
print(value)

"""



"""
Multilevel Inheritance

class A1:
    def __init__(self, n1):
        self.N1 = n1
    def show(self):
        return self.N1

class B1(A1):
    def __init__(self, n1,n2):
        super().__init__(n1)
        self.N2 = n2
    def s(self):
        return self.N1 * self.N2
    
class C1(B1):
    def __init__(self, n1,n2,n3):
        super().__init__(n1,n2)
        self.N3 = n3
    def s(self):
        return self.N1 * self.N2 * self.N3
    
r = C1(10,2,3)
value = r.s()
print(value)
"""




"""
Multiple Inheritance

class Father:
    def __init__(self, n1):
        self.N1 = n1
    def show(self):
        return self.N1

class Mother:
    def __init__(self,n2):
        self.N2 = n2
    def s(self):
        return self.N2
    
class Child(Father,Mother):
    def __init__(self, n1,n2,n3):
        Father.__init__(self,n1)
        Mother.__init__(self,n2)
        self.N3 = n3
    def s(self):
        return self.N1 * self.N2 * self.N3
    
r = Child(2,3,4)
div = r.s()
print(div)

"""
"""Hierarchical Inheritance 

# Base class
class A1:
    def __init__(self, n1):
        self.N1 = n1
    def show(self):
        return self.N1

# Derived class 1
class B1(A1):
    def __init__(self, n1, n2):
        super().__init__(n1)
        self.N2 = n2
    def s(self):
        return self.N1 * self.N2

# Derived class 2
class C1(A1):
    def __init__(self, n1, n3):
        super().__init__(n1)
        self.N3 = n3
    def s(self):
        return self.N1 + self.N3

# Creating instances of B1 and C1
hierarchical_inheritance_1 = B1(10, 2)
value1 = hierarchical_inheritance_1.s()
print("Output from B1:", value1)

hierarchical_inheritance_2 = C1(10, 3)
value2 = hierarchical_inheritance_2.s()
print("Output from C1:", value2)
"""

# # Hybrid Inheritance

# # Base class
# class A1:
#     def __init__(self, n1):
#         self.N1 = n1

# # Derived class 1
# class B1(A1):
#     def __init__(self, n1, n2):
#         A1.__init__(self, n1)
#         self.N2 = n2
# # Derived class 2
# class C1(A1):
#     def __init__(self, n1, n3):
#         A1.__init__(self, n1)
#         self.N3 = n3

# # Another derived class inheriting from B1 and C1
# class D1(B1, C1):
#     def __init__(self, n1, n2, n3, n4):
#         B1.__init__(self, n1,n2)
#         C1.__init__(self, n1,n3)
#         self.N4 = n4
#     def s(self):
#         return self.N1 * self.N2 + self.N3 * self.N4

# # Creating an instance of D1
# hybrid_inheritance = D1(10, 2, 3, 4)
# value = hybrid_inheritance.s()
# print("Output from D1:", value)

"""
Python’s Method Resolution Order (MRO) is the order in which the interpreter 
searches for the correct method implementation when a method is called on an object.
The C3 linearization algorithim offers the following proprties:

Monotonicity: If class A precedes class B in the MRO of class C, then class A also precedes class B in the MRO of any subclass of C.

Preservation of local precedence order: The order of base classes in a class definition is maintained in the MRO.

Consistency: If class A precedes class B in the MRO of one class, and class B precedes class A in the MRO of another class, 
then there is no legal MRO for their common subclass.
"""

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.C
'>, <class '__main__.A'>]

print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>)

class A:
    def my_method(self):
        return "A's method"

class B(A):
    def my_method(self):
        return "B's method"

class C(A):
    def my_method(self):
        return "C's method"

class D(B, C):
    pass

d = D()
print(d.my_method())  # Output: "B's method"

"""
In this example, when we call d.my_method(), Python searches the MRO of class D, which is [D, B, A]. 
Since D doesn’t have a my_method() implementation, Python checks the next class in the MRO, B, and finds the method. The output is "B’s method".
"""

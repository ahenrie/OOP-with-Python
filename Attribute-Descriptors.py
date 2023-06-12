"""
Attribute descriptors are a way of defining how attributes of an object are accessed, modified, or deleted.

There are three main types:
data, non-data, and property.
"""

class MinValue:
    def __init__(self, minimum):
        self.minimum = minimum
        
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
        
    def __set__(self, instance, value):
        if value < self.minimum:
            raise ValueError("Value is too small")
        instance.__dict__[self.name] = value
        
    def __set_name__(self, owner, name):
        self.name = name
"""
define a MinValue class that is a data descriptor.
__get__() method is called when the attribute is accessed
__set__() method is called when the attribute is set
__set_name__() method is called when the descriptor is assigned to an attribute in a class
The descriptor enforces a minimum value for the attribute by raising a ValueError if the value being set is smaller than the minimum.
"""
        
class MyClass:
    x = MinValue(0)


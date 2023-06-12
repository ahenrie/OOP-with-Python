"""
Map is a built in high-order function that apples a given function to all items in an input list. It returns a mapped object that can be converted 
into an iterable data structure.
SYNTAX: map(function, iterable)
"""

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))
print(squares)
# Output: [1, 4, 9, 16, 25]

"""
Filter is another built-in function that filters items from an interabe based data structure on a condition. It returns a filter object
which can be converted into a list or other iterable data structure.
SYNTAX: filter(function, iterable)
"""
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)
# Output: [2, 4]


"""
The reduce function applies a given function cumulatively to the items of an interable, reducing the iterable to a single value.
SYNTAX: functools.reduce(function, iterable[, initializer])
"""

import functools

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = functools.reduce(add, numbers)
print(sum_of_numbers)
# Output: 15


#########################################################Comparing Objectsd for Exact Match#########################################################
"""
In some cases, magical operators might bot be able to be overwritten. If that is the case with __eq__ and __ne__, 
a separate utility function can help
"""
#Define a class
class MyClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2
        
 #Create a utility function to compare objects, check for isntances and if attr are exact mathces.
def compare_objects(obj1, obj2):
    if not isinstance(obj1, MyClass) or not isinstance(obj2, MyClass):
        return False

    return obj1.attr1 == obj2.attr1 and obj1.attr2 == obj2.attr2

# Create objects
obj1 = MyClass(1, 'A')
obj2 = MyClass(1, 'A')
obj3 = MyClass(2, 'B')

# Compare objects
print(compare_objects(obj1, obj2))  # Output: True
print(compare_objects(obj1, obj3))  # Output: False

#########################################################Comparing Objectsd for Similarity#########################################################
"""
Three of the most common techniques to determine similarity:
  Euclidean Distance
  Cosine Similarity
  Jaccard Similarity
"""

#Euclidean Distance
"""
Euclidean distance is a simple way to measure the similarity between two objects in a multi-dimensional space.
It is calculated using the following formula:
                                                distance = sqrt(sum((a_i - b_i)^2 for i in range(len(a))))
"""
import math

def euclidean_distance(a, b):
    return math.sqrt(sum((a_i - b_i)**2 for a_i, b_i in zip(a, b)))

vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
distance = euclidean_distance(vector_a, vector_b)
print(distance)
# Output: 5.196152422706632

#Cosine Similarity
"""
Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space. 
It is calculated using the following formula:
                                                similarity = dot(a, b) / (norm(a) * norm(b))
"""
import numpy as np

def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
similarity = cosine_similarity(vector_a, vector_b)
print(similarity)
# Output: 0.9746318461970762

#Jaccard Similarity
"""

Jaccard similarity is a measure of similarity between two sets. It is calculated as the size of the intersection divided 
by the size of the union of the two sets. The formula is:
                                                            similarity = |A ∩ B| / |A ∪ B|
"""
def jaccard_similarity(a, b):
    set_a = set(a)
    set_b = set(b)
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    return len(intersection) / len(union)

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
similarity = jaccard_similarity(list_a, list_b)
print(similarity)
# Output: 0.2857142857142857
 
  
  
  
  
  
  
  
  
  
  
  

class TestClass:
  def sum(self, a = None, b = None, c = None, d = None, e = None):
    if (a is not None and
        b is not None and
        c is not None and
        d is not None and
        e is not None):
      return a + b + c + d + e
    elif (a is not None and
          b is not None and
          c is not None and
          d is not None):
      return a + b + c + d
    elif (a is not None and
          b is not None and
          c is not None):
      return a + b + c
    elif a is not None and b is not None:
      return a + b
    elif a is not None:
      return a
    else:
      return 0
  
obj = TestClass()
print(obj.sum())
print(obj.sum(1))
print(obj.sum(1, 2))
print(obj.sum(1, 2, 3))
print(obj.sum(1, 2, 3, 4))
print(obj.sum(1, 2, 3, 4, 5))

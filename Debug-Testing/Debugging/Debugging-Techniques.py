###################Print Statements and Logging####################
def buggy_function(a, b):
    result = a * b
    return result

# we could use an assert here
print(buggy_function(2, 3))  # Expected output: 6

#Debugging code:
import logging

logging.basicConfig(level=logging.DEBUG)

def buggy_function(a, b):
    result = a * b
    logging.debug(f"a: {a}, b: {b}, result: {result}")
    return result

print(buggy_function(2, 3))

###################Using Python Debugger (PDB)###################
"""
The Python Debugger (PDB) is a built-in debugging tool that 
allows you to interactively step through your code, examine variable 
values, and execute arbitrary Python expressions.

n (next): Execute the next line.
s (step): Step into a function call.
c (continue): Continue execution until the next breakpoint.
q (quit): Quit the debugger and exit.
p (print): Print the value of an expression.
pp (pretty-print): Pretty-print the value of an expression.
w (where): Show the current position in the code.

"""

import pdb

def buggy_function(a, b):
    result = a * b
    pdb.set_trace()
    return result

print(buggy_function(2, 3))

# functions ----------

from collections import Iterable

def print_msg():
    """
This is a python function!
Printing Hello World.
    """
    print("Hello World")

print(dir(print_msg))
#print(print.__main__)
print("--------------")
print(print_msg.__doc__)
print_msg()
print(print_msg.__str__)

print(isinstance(dir(print_msg), Iteratable))

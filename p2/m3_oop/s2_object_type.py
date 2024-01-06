"""
Python Course - Part 2

https://github.com/egalli64/pyco

Module 3 - More on Object Oriented Programming

The classes object and type
"""


class A(object):
    pass


class B:
    pass


print(f"The {A.__name__} base class is {A.__base__}")
print(f"The {B.__name__} base class is {B.__base__}")

print("\n*** The object attributes:")
for cur in dir(object):
    print(cur)
print()

# the metaclass type is-a object
print(f"{type.__name__}, that extends {type.__base__}, is callable?", callable(type))
print("*** The type attributes:")
for cur in dir(type):
    print(cur)

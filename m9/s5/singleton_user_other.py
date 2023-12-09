"""
Python Course

https://github.com/egalli64/pyco

Module 9 - Design Pattern

Singleton (by module)
"""
import singleton


def singleton_increaser():
    """A function that change the singleton state"""
    singleton.value += 1


if __name__ == "__main__":
    print("Meant to be imported by user")

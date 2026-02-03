#!/usr/bin/python
"""Construct a FlyingFish class that inherits from both
a Fish class and a Bird class."""


class Fish:
    """Create a Fish class with two methods"""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Create a Bird class with two methods"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A FlyingFish class that inherits from both Fish and Bird"""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


print(FlyingFish.mro())

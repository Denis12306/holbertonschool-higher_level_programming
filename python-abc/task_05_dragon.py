#!/usr/bin/python
"""Design two mixin classes, SwimMixin and FlyMixin, each equipped with methods
swim and fly respectively. Next, construct a class Dragon that inherits from
both these mixins. Your aim is to show that a Dragon instance can both
swim and fly."""


class SwimMixin:
    """Define the Mixin Swim class"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Define the Mixin Fly class"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Define the Dragon class with 2 previous class"""

    def roar(self):
        print("The Dragon roars!")

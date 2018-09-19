"""Example of a cyclic reference that can be resolved in both python3 and python2"""
import gc

class A:
    def __init__ (self, name):
        self.name = name
        self.other = None
    def set_other(self, other):
        self.other = other
    def __repr__(self):
        return "A({})".format(self.name)

a1 = A("first")
a2 = A("second")
a3 = A("third")
a1.set_other(a2)
a2.set_other(a3)
a3.set_other(a1)

a1 = a2 = a3 = None
n = gc.collect()
print("Number of unreachable objects {}".format(n))

print("items that couldn't be cleaned up: {}".format(gc.garbage))

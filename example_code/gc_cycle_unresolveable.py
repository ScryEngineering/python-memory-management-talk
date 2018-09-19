"""Example of a cyclic reference that can't be resolved in Python 2 but can be resolved in python3.
See PEP 422 https://www.python.org/dev/peps/pep-0442/ for details on why this changed"""
import gc

class B:
    def __init__ (self, name):
        self.name = name
        self.other = None
    def set_other(self, other):
        self.other = other
    def __repr__(self):
        return "B({})".format(self.name)
    def __del__(self):
        print('{}.__del__()'.format(self))

b1 = B("first")
b2 = B("second")
b3 = B("third")
b1.set_other(b2)
b2.set_other(b3)
b3.set_other(b1)


b1 = b2 = b3 = None
n = gc.collect()
print("Number of unreachable objects {}".format(n))

print("items that couldn't be cleaned up: {}".format(gc.garbage))

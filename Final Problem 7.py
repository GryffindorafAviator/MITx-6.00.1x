# Problem 7
# 20/20 points (graded)
# You are given the following superclass. Do not modify this.

# class Container(object):
#     """ Holds hashable objects. Objects may occur 0 or more times """
#     def __init__(self):
#         """ Creates a new container with no objects in it. I.e., any object 
#             occurs 0 times in self. """
#         self.vals = {}
#     def insert(self, e):
#         """ assumes e is hashable
#             Increases the number times e occurs in self by 1. """
#         try:
#             self.vals[e] += 1
#         except:
#             self.vals[e] = 1
#     def __str__(self):
#         s = ""
#         for i in sorted(self.vals.keys()):
#             if self.vals[i] != 0:
#                 s += str(i)+":"+str(self.vals[i])+"\n"
#         return s

# Write a class that implements the specifications below. Do not override any methods of Container.

# class ASet(Container):
#     def remove(self, e):
#         """assumes e is hashable
#            removes e from self"""
#         # write code here
# 
#     def is_in(self, e):
#         """assumes e is hashable
#            returns True if e has been inserted in self and
#            not subsequently removed, and False otherwise."""
#         # write code here

# For example,
# d1 = ASet()
# d1.insert(4)
# d1.insert(4)
# 
# d1.remove(2)
# print(d1)
# 
# d1.remove(4)
# print(d1)

# prints
# 4:2 # from d1.remove(2) print

#     # (empty) from d1.remove(4) print

# For example,
# d1 = ASet()
# d1.insert(4)
# print(d1.is_in(4))
# d1.insert(5)
# print(d1.is_in(5))
# d1.remove(5)
# print(d1.is_in(5))

# prints
# True
# True
# False

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        try:
            del self.vals[e]
        except:
            pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        try:
           if self.vals[e] != 0:
            return True
           else:
            return False
        except:
            return False

d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)

d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))

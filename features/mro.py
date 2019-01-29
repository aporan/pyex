# helpful links:
# https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc
# https://www.python.org/download/releases/2.3/mro/

# python3 

class A:

    def __init__(self):
        print("I'm A")

    def unimplemented(self):
        raise NotImplementedError("A's method not implemented")


class B:

    @classmethod
    def make(cls):
        print("I'm making B")


class C(A, B):

    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    c = C()
    print(C.mro()) # L[C] = C A B O

    # contains both the implemented functions; some dependency
    # functions will not called only depending on the mro. In this
    # case, the functions are different, so it is not a problem.
    # example in ''' below.
    print(dir(c))


"""
class A:
	def whereiam(self):
		print "I am in A"

		
class B(A):
	def whereiam(self):
		print "I am in B"

		
class C(A):
	def whereiam(self):
		print "I am in C"
		
		
class D(B, C):
	def whereiam(self):
		print "I am in D"

>>>d = D()
>>>d.whereiam()
I am in D

######

class A:
	def whereiam(self):
		print "I am in A"

		
class B(A):
	def whereiam(self):
		print "I am in B"

		
class C(A):
	def whereiam(self):
		print "I am in C"
		
		
class D(B, C):
    pass

>>>d = D()
>>>d.whereiam()
I am in B

######

remove the method from B and check what happens. It is
supposed to print “ I am in A”. 

Again remove the method from A and you will see it prints “ I am in
C”. 

L[B] = BAO
L[C] = CAO
L[D] = D + merge(L[B] + L[C] + BC)
     = D + merge(BAO + CAO + BC)
     = D + B + merge(AO + CAO + C)
     = find the result
"""    
    

    

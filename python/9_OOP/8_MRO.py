#MRO (Method Resolution order)
class A:
    lable = "A: Base class"

class B(A):
    lable = "B: Masala blend"

class C(A):
    lable = "C: Masoori blend"

class D(B,C):
    pass

cup = D()
print(cup.lable)
print(D.__mro__)
class Bi(A,C):
    pass
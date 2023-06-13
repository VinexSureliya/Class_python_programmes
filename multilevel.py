class A():
    x,y=10,20
class B(A):
    a,b = 30,40
class C(A):
    p,q = 50,60
class D(A):
    h,i  = 80,90
b1 = B()
print(b1.x,b1.y,b1.a,b1.b)
c1 = C()
print(c1.x,c1.y,c1.p,c1.q)
d1 = D()
print(d1.x,d1.y,d1.h,d1.i)
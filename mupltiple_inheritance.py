class A():
    x,y=10,20
class B():
    a,b = 30,40
class C_Class(A,B):
    p,q = 50,60

c1 = C_Class()
print(c1.x,c1.y,c1.a,c1.b,c1.p,c1.q)

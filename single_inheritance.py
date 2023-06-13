class P_Class:
    x = 10
    y = 20
class C_Class(P_Class):
    a = 100
    b = 200

p1 = P_Class()
print(p1.x,p1.y)

c1 = C_Class()
print(c1.a,c1.b,c1.x,c1.y)
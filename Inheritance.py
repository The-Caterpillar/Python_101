class A:
    def method(self):
        print("Inside A")
class B:
    def method(self):
        print("Inside B")
class C:
    def method(self):
        print("Inside C")
class D(B,C):
    pass

d = D()
e = D.mro()
d.method()

for cls in e:
    print(cls,end=" ")
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img  = img
    def print(self):
        print(str(self.real)+" "+str(self.img)+"i")
    def add(self,c):
        self.real += c.real
        self.img = self.img + c.img

c1 = complex(10,20)
c1.print()

c2 = complex(20,30)
c2.print()

c1.add(c2)
c1.print()
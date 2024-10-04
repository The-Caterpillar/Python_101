class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def prints(self):
        print("real = ",self.real," img = ",self.img)
        print(self.real," + ",self.img,"i")
    def add(self,c):
        self.real = self.real + c.real
        self.img = self.img + c.img


c1 = complex(5,4)
c1.prints()
c2 = complex(10,11)
c2.prints()

c1.add(c2)
c1.prints()
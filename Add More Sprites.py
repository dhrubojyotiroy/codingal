class myobject:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __index__(self):
        return self.x + self.y


obj = myobject(8,4)
print(bin(obj))

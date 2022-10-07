#Program to find properties of shapes(circle,triangle,square and rectangle)
class Shape:
    def __init__(self,radius,side,base,height,length,width):
        self.side = side
        self.radius = radius
        self.base = base
        self.height = height
        self.length = length
        self.width = width
        self.storage= []
    def circle(self):
        return 3.142*self.radius**2
    def triangle(self):
        return 0.5*self.base*self.height
    def square(self):
        return self.side**2
    def rectangle(self):
        return self.length*self.width
    
    def __repr__(self):
        return "\nThe area in each: \n Circle {} \n triangle: {} \n Square: {} \n rectangle {}".format(self.circle(), self.triangle(),self.square(),self.rectangle())
    
def main():
    shape = Shape(49,4,4,8,2,6)
    # shape.circle()
    # shape.triangle()
    # shape.square()
    # shape.rectangle()
    print(shape)
    
main()

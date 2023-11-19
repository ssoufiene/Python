class Rectangle :
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,x):
        self.width=x
    def set_height(self,y):
        self.height=y
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return (((self.width)**2)+((self.height)**2))**0.5
    def get_picture(self):
        if self.height >50 or self.width> 50 :
            return  "Too big for picture."
        else :
            a=''
            for i in range(self.height):
                k=self.width*'*'
                a=a+f'{k}\n'
        return a

    def get_amount_inside(self,shape):
        v = self.get_area()
        w=shape.get_area()
        if w > v :
            return 0
        else:
            if shape.height<self.height:
                return int(v/w)
            else :
                return 0
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(self,length)
        self.width=length
        self.height=length

    def set_side(self,z):
        self.length=z
        self.width = self.length
        self.height = self.length
    def __str__(self):
        return f'Square(side={self.width})'

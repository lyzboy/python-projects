from math import sqrt, pow, floor

class Rectangle():
    """Class for creating Rectangles"""
    def __init__(self,width:int, height:int)->None:
        self._width = width
        self._height = height

    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'

    @property
    def width(self)->int:
        return self._width
    @property
    def height(self)->int:
        return self._height
    
    def set_width(self, width:int)->None:
        print(f'Setting width to {width}')
        self._width = width
    
    def set_height(self, height:int)->None:
        print(f'Setting height to {height}')
        self._height = height

    def get_area(self)->int:
        return self._width * self._height
    
    def get_perimeter(self)->int:
        return 2 * (self._width + self._height)
    
    def get_diagonal(self)->float:
        return sqrt(pow(self._width, 2) + pow(self._height, 2))
    def get_picture(self)->str:
        if max(self._width, self._height) > 50:
            return 'Too big for picture.'
        return_string = ""
        for y in range(self._height):
            for x in range(self._width):
                return_string += "*"
            return_string +="\n"
        return return_string
    
    def get_amount_inside(self,other)->int:
        return (floor(self._width / other.width) * floor(self._height / other.height))
    

class Square(Rectangle):
    """Creates a Square object with base Rectangle"""
    def __init__(self,width:int)->None:
        super().__init__(width, width)
    
    def set_width(self, value:int)->None:
        self._width = self._height = value

    def set_height(self, value:int)->None:
        self._width = self._height = value
    
    def set_side(self, value:int)->None:
        self._width = self._height = value
    
    def __str__(self)->str:
        return f'Square(side={self._width})'

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
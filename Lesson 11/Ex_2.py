class Rect:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.area = height * width

    @staticmethod
    def add_area(rect1, rect2):
        return rect1.area + rect2.area

x = Rect(2, 4)
y = Rect(4, 3)

print(Rect.add_area(x, y))
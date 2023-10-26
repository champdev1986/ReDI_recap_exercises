class Rect:
    def __init__ (self, h, w) :
        self.h = h
        self.w = w
        self.area = h * w

x = Rect(3, 4)
x.w = 0

print(x.area)

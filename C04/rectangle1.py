

Skip to content
Using Gmail with screen readers
Conversations
Get started with Gmail
Customize your inbox
Change profile image
Import contacts and mail
Get Gmail for mobile
     
0% of 15 GB used
Terms · Privacy · Program Policies
Last account activity: 2 days ago
Details
rectangle1.py

class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def area(self):
        return self.l * self.b

    def peri(self):
        return 2 * (self.l + self.b)
    def compare(self, obj2):
        if self.area() == obj2.area():
            print("Both areas are equal.")
        elif self.area() > obj2.area():
            print("Area of the 1st rectangle is greater.")
        else:
            print("Area of the 2nd rectangle is greater.")

l1 = int(input("Enter the length of first rectangle: "))
b1 = int(input("Enter the breadth of first rectangle: "))
l2 = int(input("Enter the length of second rectangle: "))
b2 = int(input("Enter the breadth of second rectangle: "))
obj1 = Rectangle(l1, b1)
obj2 = Rectangle(l2, b2)
print("Area of rectangle 1:", obj1.area())
print("Perimeter of rectangle 1:", obj1.peri())
print("Area of rectangle 2:", obj2.area())
print("Perimeter of rectangle 2:", obj2.peri())
obj1.compare(obj2)

Displaying rectangle1.py.

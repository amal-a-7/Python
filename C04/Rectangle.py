class Rectangle:
    def __init__(self):
        self.__l=int(input("Enter the length: "))
        self.__b=int(input("Enter the breadth: "))
    def __lt__(ob1,ob2):
          area1=ob1.__l*ob1.__b
          area2=ob2.__l*ob2.__b
          print("Area of Recatangle is:",area1)
          print("Area of recatangle is :",area2)
          return area1<area2
        
print("Enter the length and breadth of first object:")
ob1=Rectangle()
print("Enter the length and breadth of second object: ")
ob2=Rectangle()
if ob1<ob2:
    print("Rectangle1 is less than Rectangle2: ")
else:
    print("rectangle1 is greater than or equal to rectangle2: ")

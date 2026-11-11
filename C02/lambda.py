square = lambda a: a * a 
rectangle = lambda l, b: l * b 
triangle = lambda b, h: 0.5 * b * h 
 
side=float(input("Enter side of square:")) 
print("Area of Square:", square(side)) 
l=float(input("Enter length of rectangle:")) 
b=float(input("Enter breadth of rectangle:")) 
print("Area of Rectangle:", rectangle(l,b)) 
base=float(input("Enter base of triangle:")) 
height=float(input("Enter height of triangle:")) 
print("Area of Triangle:", triangle(base, height)) 

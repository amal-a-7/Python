a = input("Enter first string: ") 
b = input("Enter second string: ") 
x = a[1] 
y = b[1] 
a = a[0] + y + a[2:] 
b = b[0] + x + b[2:] 
print(a + " " + b)

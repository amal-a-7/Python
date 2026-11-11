x = a = int(input("Enter first number: ")) 
y = b = int(input("Enter second number: ")) 
while b != 0: 
   a, b = b, a % b 
print("GCD of", x, ",", y, "=", a) 

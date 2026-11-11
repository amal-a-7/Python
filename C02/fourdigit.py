a = int(input("Enter starting number: ")) 
b = int(input("Enter ending number: ")) 
 
for n in range(a, b + 1): 
    if int(n**0.5)**2==n: 
        s=str(n) 
        if all(int(d)%2==0 for d in s): 
            print(n) 

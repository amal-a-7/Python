numbers = list(map(int, input("Enter integers: ").split())) 
result = [] 
for x in numbers: 
   if x % 2 != 0: 
       result.append(x) 
print("List after removing even numbers:", result)

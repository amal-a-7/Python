s = input("Enter a string: ") 
for i in sorted(set(s)): 
   print(f"{i} : {s.count(i)}") 

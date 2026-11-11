number = input("Enter the integers: ") 
number = [int(x) for x in number.split()] 
result = [] 
for n in number: 
  if n > 100: 
    result.append("over") 
  else: 
    result.append(n) 
print(result) 

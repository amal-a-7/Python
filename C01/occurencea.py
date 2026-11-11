names = input("Enter first names: ").split() 
count = 0 
for name in names: 
    count = count + name.lower().count('a') 
print("Occurrences of 'a':", count)

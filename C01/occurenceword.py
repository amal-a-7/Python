s = input("Enter a line: ") 
words = s.split() 
for word in set(words): 
    print(word, ":", words.count(word)) 

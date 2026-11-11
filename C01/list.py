numbers = [i for i in [-3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if i > 0] 
print("Positive numbers:", numbers) 
 
square = [n * n for n in numbers] 
print("Square of numbers:", square) 
 
word=input("Enter a word:") 
vowels=[i for i in word if i in "a,e,i,o,u,A,E,I,O,U"] 
print("Vowels are:",vowels) 
 
wrd = input("Enter a word: ") 
ordinal_values = [ord(char) for char in wrd] 
print("Ordinal values:", ordinal_values) 



Skip to content
Using Gmail with screen readers
Conversations
Get started with Gmail
Customize your inbox
Change profile image
Import contacts and mail
Get Gmail for mobile
     
0% of 15 GB used
Terms · Privacy · Program Policies
Last account activity: 2 days ago
Details
book.py

class Publisher:
    def __init__(self ,name):
        self.name = name
    
    def display(self):
        print("Publisher name",self.name)

class Book(Publisher):
    def __init__(self ,name,title,author):
        Publisher.__init__(self,name)
        self.title = title
        self.author = author
        
    def display(self):
        print("author name ",self.author)
        print("title name ",self.title)        
        
class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        Book.__init__(self,name,title,author)
        self.price = price
        self.no_of_pages = no_of_pages
        
    def display(self):
        Publisher.display(self)
        Book.display(self)
        print("price amount ",self.price)
        print("number of pages ",self.no_of_pages)
        
n = input("publisher name:")
t = input("enter the title:")
a = input("enter the author name :")
p = float(input("enter the price of the book:"))
np = int(input("enter the number of pages:"))
obj = Python(n,t,a,p,np)
obj.display()

Displaying book.py.

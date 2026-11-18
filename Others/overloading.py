 class A:
     def __init__(self, a):
         self.a = a
 
     # Adding two objects
     def __sub__(self, o):
         return self.a - o.a
 
 
 ob1 = A(1)
 ob2 = A(2)
 ob3 = A("Geeks")
 ob4 = A("For")
 
 print(ob1 - ob2)
 print(ob3  - ob4)

///greatest///

class A:
    def __init__(self,a):
        self.a = a
        
    def __lt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False
        
ob1 = A(2)
ob2 = A(3)
if(ob1>ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob2")

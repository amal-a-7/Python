            #polymorphism-operator overloading                          
 
  A="hello"
  B="how are you?"
  print(A+B)
  C=10
  D=20
  print(C+D)

            #method overloading

 class moverload:
     def display(self,a=None,b="Done"):
         print(a,b)
 obj=moverload()
 obj.display()
 obj.display(10)
 obj.display(10,20)

            #method overriding

 class father():
     def transportation(self):
         print("Cycle")
 class son(father):
     def transportation(self):
         print("Bike")
 obj=son()
 obj.transportation()

            #data encapsulation

 class encap:
     a=10
     def display(self):
         print("welcome")
 obj=encap()
 print(obj.a)
 obj.display()



class encap:
     __a=10#private variable
    def display(self):
        print("welcome")
        print(self.__a)
obj=encap()
obj.display()




class vehicle:
    def start(self):
        print("the vehiche is started ")
    
    def acceletare(self):
        print("the vechicle is accelarated ")
    
    def breaks(self):
        print("the vechicle is now breaked")
     
     
class transpo(vehicle):
    def tanspodis(self):
        print("tansport details")

class passenger(vehicle):
    def passdis(self):
        print("passenger info")
    
    
class van(transpo):
     def loadvan(self):
         print("the loads in van ")

class truck(transpo):
    def loadcontainer(self):
        print("the loads of container")
        
class bike(passenger):
    def bikedisplay(self):
        print("bike info")
      
class car(passenger):
    def cardisplay(self):
        print("car info")
        
v = van()
t = truck()
b = bike()
c = car()

v.loadvan()
v.tanspodis()
v.start()
v.acceletare()
v.breaks()
print(" ")

t.loadcontainer()
t.tanspodis()
t.start()
t.acceletare()
t. breaks()
print(" ")

c.cardisplay()
c.passdis()
c.start()
c.acceletare()
c.breaks()
print(" ")

b.bikedisplay()
b.passdis()
b.start()
b.acceletare()
b.breaks()



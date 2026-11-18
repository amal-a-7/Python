class student:
    rno=123
    name="Honey"
    branch="MCA"
    
    def read(self):
        rno=550
        print('Roll no is=',rno)
        print('instance variable=',self.rno)
        print("Welcome to my class")
        
        #object outside class
        
obj=student()
print("rno=",obj.rno)
print("name=",obj.name)
print("branch=",obj.branch)
obj.read()


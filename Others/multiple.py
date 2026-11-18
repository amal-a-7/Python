class father:
    def fdisplay(self):
        print("father")
class mother:
    def mdisplay(self):
        print("mother")
class child(father,mother):
    def cdisplay(self):
        print("child")
        
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.fdisplay()


class grandparent:
    def display(self):
        print("grandparent class")
class parent(grandparent):
    def show(self):
        print("parent class")
class child(parent):
    def cdisplay(self):
        print("child  class")
c=child()
c.display()
c.show()
c.cdisplay()

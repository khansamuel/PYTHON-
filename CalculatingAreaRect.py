class Rectangle:
  def __init__(self,length,width):
    self.length =length
    self.width=width
  def area(self):
    return self.length*self.width
  
  def perimeter(self):
    return 2*(self.length+self.width)
  
len= int(input("Enter length:"))
win=int(input("Enter width:"))

rect=Rectangle(len,win)
print("Area is",rect.area())
print("Perimeter is",rect.perimeter())   

  
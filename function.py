#python function 
def calculate_rectangle_area(length ,width):
  if length <= 0 or width <=0 :
    raise ValueError("Length and width must be positive numbers.")
  area= length * width
  return area 
  
length= 5
width = 6
area=calculate_rectangle_area(length ,width)
print("The area of the rectangle is :",area)

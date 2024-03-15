class Temperature:
   def __init__(self,celsius):
     self.celsius=celsius
     
   def celcius(self):
    return((self.celsius *1.8) +32)
  
   
cel= int(input("Celsius:"))


Temp=Temperature(cel)
print("Temperature in farhrenheit ",Temp.celcius())



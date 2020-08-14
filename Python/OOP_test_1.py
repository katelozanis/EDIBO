class PartyAnimal:
   x = 0
   


   

#__init__metode tiks izpildīta tikai vienu
# reizi, veidojot (katru) instanci
   def __init__(self):
      print("I am constructed")
      self.x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far x propery of object",\
           "is: ",self.x)

   def __del__(self):
         print('I am dectructed', self.x)

     
print("Before an = PartyAnimal()")
#print(vars())
an = PartyAnimal()
print("After an =PartyAnimal()")
#print(vars())
#print("an data type:", type(an))
#print("an methods and properties:", dir(an))
#print("an x property data type: ", type(an.x))
#print("an party method data type:", type(an.party))
#print(vars(an))
# tikai ja klase or ar __init__ un ar self.x
#tikai tad {'x':0}:, savādāk ir {}




print("\nBefore first an.party()")
an.party()
print("After first an.party()")
#print(vars(ab))# objekts "aiztikts" {'x':


an.x=100
an.__init__()


print("\nBefore second an.party()")
an.party()
print("After second an.party()")

an.x =200

print("\nbefore third an.part()")
an.party()
print("After third an.party()")

print("\nBefore one more party()")
PartyAnimal.party(an)
print("After one more party()")


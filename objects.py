#inp = input('Europe floor?')
#usf = int(inp) + 1
#print('US floor', usf)

class PartyAnimal:
    x = 0

    def party(self) :
      self.x = self.x + 1
      print("So far",self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

# Skriver ut alle muligheter til et objekt (streng, lister, objecter osv)
#print(dir(an))

class PartyAnimal:
   x = 0

   def __init__(self):
     print('I am constructed') 

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):  # Når objektet blir slettet, endret til f eks integer så kjøres denne
     print('I am destructed', self.x)

an = PartyAnimal()          # Her kjøres constructor
an.party()
an.party()
an = 42                     # Her kjøres destructor
print('an contains',an)


class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, z):
     self.name = z
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()


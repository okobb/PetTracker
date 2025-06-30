class Pet:
  # Constructor for pet class
  def __init__(self,name, species, age):
    self.name = name
    self.species  = species
    self.age = age
    self.adopted = False
   
  # function to display pet info  
  def display_info(self):
      print(f"Pet name: {self.name}, Pet species: {self.species}, Pet Age: {self.age}, Adopted: {self.adopted}")
      
  def mark_adopted(self):
      self.adopted = True
    
  def birthday(self):
      self.age += 1
    
bobby = Pet("Bobby" , "Cat" , 5)
max = Pet("Max" , "Dog" , 8)
woody = Pet("Woody" , "Bird" , 10)

bobby.display_info()
max.display_info()
woody.display_info()

max.birthday()
max.mark_adopted()
max.display_info()
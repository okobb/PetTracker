class Pet:
  # Created a constructor for pet class
  def __init__(self,name, species, age):
    self.name = name
    self.species  = species
    self.age = age
    self.adopted = False
   
  # Created a function to display pet info  
  def display_info(self):
      print(f"Pet name: {self.name}, Pet species: {self.species}, Pet Age: {self.age}, Adopted: {self.adopted}\n")
      
  # Created a function to set the pet as adopted    
  def mark_adopted(self):
      self.adopted = True
      
  # Created a function to increase age by one 
  def birthday(self):
      self.age += 1
      
# Created objects for testing purposes    
bobby = Pet("Bobby" , "Cat" , 5)
max = Pet("Max" , "Dog" , 8)
woody = Pet("Woody" , "Bird" , 10)

# Displaying the info of created pets
bobby.display_info()
max.display_info()
woody.display_info()

# Testing and showing the results of created functions
max.birthday()
max.mark_adopted()
max.display_info()

# Created a manual pet list
pets = [{"name" : "Simon" , "species" : "Cat" , "age" : 7, "adopted" : False},
        {"name" : "Rex" , "species" : "Dog" , "age" : 9, "adopted" : True},
        {"name" : "Tweety" , "species" : "Bird" , "age" : 3, "adopted" : False}]

# Created a function to find non-adopted pets
def find_non_adopted(list):
    found  = []
    for pet in list:
        if pet["adopted"] == True:
            found.append(pet["name"])
    
    if len(found) == 1:
        print(found[0] + " is the only adopted pet in this list.\n")
    else:
        print("The adopted pets are: " )
        for name in found:
            print (str(name))
        print("\n")
     
find_non_adopted(pets)


class Pet:
  # Creating a constructor for pet class
  def __init__(self,name, species, age):
    self.name = name
    self.species  = species
    self.age = age
    self.adopted = False
   
  # Creating a method to display pet info  
  def display_info(self):
      print(f"Pet name: {self.name}, Pet species: {self.species}, Pet Age: {self.age}, Adopted: {self.adopted}\n")
      
  # Creating a method to set the pet as adopted    
  def mark_adopted(self):
      self.adopted = True
      
  # Creating a method to increase age by one 
  def birthday(self):
      self.age += 1
  # Creating a method to increase rename pet 
  def rename(self, new_name):
      self.name = new_name
      
# Creating objects for testing purposes    
cat = Pet("Bobby" , "Cat" , 5)
dog = Pet("Max" , "Dog" , 8)
bird = Pet("Woody" , "Bird" , 10)

# Displaying the info of created pets
cat.display_info()
dog.display_info()
bird.display_info()

# Testing and showing the results of created functions
dog.birthday()
dog.mark_adopted()
dog.display_info()

# Creating a manual pet list
pets = [{"name" : "Simon" , "species" : "Cat" , "age" : 7, "adopted" : False},
        {"name" : "Rex" , "species" : "Dog" , "age" : 9, "adopted" : True},
        {"name" : "Tweety" , "species" : "Bird" , "age" : 3, "adopted" : False}]

# Creating a function to find non-adopted pets
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

# Testing the created function  
find_non_adopted(pets)

# Testing rename method
cat.rename("Garfield")
cat.display_info()


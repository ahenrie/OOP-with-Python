#Storing Objects in Lists
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

dogs = []
dog0 = Dog("Marceline", "German Shepherd")
dog1 = Dog("Cajun", "Belgian Malinois")
dog2 = Dog("Daisy", "Border Collie")
dog3 = Dog("Rocky", "Golden Retriever")
dog4 = Dog("Bella", "Irish Setter")

dogs.append(dog0)
dogs.append(dog1)
dogs.append(dog2)
dogs.append(dog3)
dogs.append(dog4)

for dog in dogs:
  print(dog.name)
  print(dog.breed)

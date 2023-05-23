class Airplane:
  def __init__(self, first_class, business_class, coach):
    self.first_class = first_class
    self.business_class = business_class
    self.coach = coach

  def total(self):
      return self.first_class + self.business_class + self.coach
  
class Train:
  def __init__(self, car1, car2, car3, car4, car5):
    self.car1 = car1
    self.car2 = car2
    self.car3 = car3
    self.car4 = car4
    self.car5 = car5
  
  def total(self):
    return self.car1 + self.car2 + self.car3 + self.car4 + self.car5

def passengers(obj):
  print(f'There are {obj.total()} passengers on board.')

Train1 = Train(1, 2, 3, 4, 5)
Airplane1 = Airplane(1, 2, 3)

passengers(Train1)
passengers(Airplane1)

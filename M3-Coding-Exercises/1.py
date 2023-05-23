class CelestialBody:
  def __init__(self, size, mass, composition, name):
    self.size = size
    self.mass = mass
    self.composition = composition
    self.name = name
    
# create the satellite class
class Satellite(CelestialBody):
  def __init__(self, size, mass, composition, name, host_planet):
    super().__init__(size, mass, composition, name)
    self.host_planet = host_planet

# create the planet class
class Planet(CelestialBody):
  def __init__(self, size, mass, composition, name, host_star):
    super().__init__(size, mass, composition, name)
    self.host_star = host_star

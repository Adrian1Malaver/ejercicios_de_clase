class Animal:
  def __init__(self, raza, edad, peso):
    self.raza=raza
    self.edad=edad
    self.peso=peso
  def saludar(self):
    pass
  def mostrar_informacion(self):
    return (self.raza, self.edad, self.peso)
class Gato(Animal):
  def saludar(self):
    return "miau"
class Perro(Animal):
  def saludar(self):
   return "guau"
class Pez(Animal):
  def saludar(self):
    return "glu"
class Ave(Animal):
  def saludar(self):
    return "rua"
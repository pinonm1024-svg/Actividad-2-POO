# Se genero la clase en este caso fueron perros
class Perro:
    # Cada perro nace con una descripcion general
    def __init__(self, raza_perro, talla_perro, color_perro):
        self.raza = raza_perro
        self.talla = talla_perro
        self.color = color_perro
    # Se genero la accion a realizar
    def mostrar_ficha(self):
        print(f"El perro es de raza {self.raza} de tamaño {self.talla} y de color {self.color}")
perro1 = Perro("chihuahua", "chico", "negro")
perro2 = Perro("pitbul", "mediano", "dorado")
perro3 = Perro("doverman", "grande", "cafe")
perro4 = Perro("labrador", "mediano", "blanco")

perro1.mostrar_ficha()
perro2.mostrar_ficha()
perro3.mostrar_ficha()
perro4.mostrar_ficha()

class Gato:
    def __init__(self, raza_gato, talla_gato, color_gato):
        self.raza = raza_gato
        self.talla = talla_gato
        self.color = color_gato
    def mostrar_ficha(self):
        print(f"El gato es de raza {self.raza} de tamaño {self.talla}, de color {self.color}")
gato1 = Gato("siames", "chico", "dorado")
gato2 = Gato("montes", "grande", "gris")
gato3 = Gato("persa", "mediano", "blanco")
gato4 = Gato("siberiano", "grande", "cafe")

gato1.mostrar_ficha()
gato2.mostrar_ficha()
gato3.mostrar_ficha()
gato4.mostrar_ficha()
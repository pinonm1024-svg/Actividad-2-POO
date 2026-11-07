# ==============================================================================
# ACTIVIDAD FORMATIVA 3: HERENCIA
# Autores: Miguel Angel Piñon Valdez
# Descripción: Implementación de herencia utilizando la clase base Animal
#              y las subclases derivadas Perro y Gato.
# ==============================================================================

# 1. CLASE BASE (Superclase)
class Animal:
    """
    Clase base que agrupa atributos y métodos generales para ser heredados
    por otras clases derivadas, evitando la duplicidad de código.
    """
    def __init__(self, raza, talla, color):
        # Atributos compartidos por todos los animales
        self.raza = raza
        self.talla = talla
        self.color = color

    def mostrar_ficha(self):
        """Método base para desplegar los datos generales de la mascota."""
        print(f"Es de raza {self.raza}, de tamaño {self.talla} y de color {self.color}.")


# 2. CLASES DERIVADAS (Subclases)

class Perro(Animal):
    """
    Clase derivada Perro. Hereda de Animal y agrega comportamientos
    y atributos propios de los caninos.
    """
    def __init__(self, raza, talla, color, sonido="Guau guau"):
        # Se reutiliza el constructor de la superclase mediante super()
        super().__init__(raza, talla, color)
        self.sonido = sonido  # Atributo exclusivo de la subclase

    def mostrar_ficha(self):
        """Sobrescritura (Override) del método de la clase base."""
        print(f"[PERRO] El can es de raza {self.raza}, tamaño {self.talla}, color {self.color}.")

    def hacer_sonido(self):
        """Método propio y exclusivo de la clase Perro."""
        print(f"   -> Sonido: El perro hace '{self.sonido}'.")


class Gato(Animal):
    """
    Clase derivada Gato. Hereda de Animal y agrega comportamientos
    y atributos propios de los felinos.
    """
    def __init__(self, raza, talla, color, sonido="Miau"):
        # Se reutiliza el constructor de la superclase mediante super()
        super().__init__(raza, talla, color)
        self.sonido = sonido  # Atributo exclusivo de la subclase

    def mostrar_ficha(self):
        """Sobrescritura (Override) del método de la clase base."""
        print(f"[GATO] El felino es de raza {self.raza}, tamaño {self.talla}, color {self.color}.")

    def hacer_sonido(self):
        """Método propio y exclusivo de la clase Gato."""
        print(f"   -> Sonido: El gato hace '{self.sonido}'.")


# ==============================================================================
# 3. PROGRAMA PRINCIPAL (Instanciación y Pruebas)
# ==============================================================================
if __name__ == "__main__":
    print("==========================================")
    print("      PRUEBA DE INSTANCIAS DE PERROS      ")
    print("==========================================")
    perro1 = Perro("Chihuahua", "Chico", "Negro", "Guau pequeño")
    perro2 = Perro("Pitbull", "Mediano", "Dorado")
    perro3 = Perro("Dóberman", "Grande", "Café")
    perro4 = Perro("Labrador", "Mediano", "Blanco")

    # Demostración de métodos sobrescritos y exclusivos
    perro1.mostrar_ficha()
    perro1.hacer_sonido()
    perro2.mostrar_ficha()
    perro2.hacer_sonido()
    perro3.mostrar_ficha()
    perro4.mostrar_ficha()

    print("\n==========================================")
    print("      PRUEBA DE INSTANCIAS DE GATOS       ")
    print("==========================================")
    gato1 = Gato("Siamés", "Chico", "Dorado", "Miau agudo")
    gato2 = Gato("Montés", "Grande", "Gris")
    gato3 = Gato("Persa", "Mediano", "Blanco")
    gato4 = Gato("Siberiano", "Grande", "Café")

    # Demostración de métodos sobrescritos y exclusivos
    gato1.mostrar_ficha()
    gato1.hacer_sonido()
    gato2.mostrar_ficha()
    gato2.hacer_sonido()
    gato3.mostrar_ficha()
    gato4.mostrar_ficha()


class Perro:
    especie = "Canis lupus familiaris"
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
     #constructor para inicializar los atributos del perro
    def __init__(self, nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    #método para imprimir los datos del perro
    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} edad")

    def main():
        perro1 = Perro("Max", "Labrador", 5)
        perro1.imprimirDatos()
        perro2 = Perro("Bella", "Golden Retriever", 3)
        perro2.imprimirDatos()
        perro3 = Perro("max", "Bulldog", 7)
        perro3.imprimirDatos()
        perro4 = Perro("Dante",)
        perro4.imprimirDatos()
        perro2 = Perro("Pastor belga", )
        perro2.imprimirDatos()
        perro5 = Perro("Raya", "siames", 1)
        perro5.imprimirDatos()

if __name__ == "__main__":
    "main"
        
        

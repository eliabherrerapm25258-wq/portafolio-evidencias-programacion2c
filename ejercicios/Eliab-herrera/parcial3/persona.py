"""
crea una clase persona con los siguientes atributos: nombre, edad, genero y nacionalidad.
agrega un método para imprimir los datos de la persona y otro método para calcular el año
de nacimiento de la persona.
crea un objeto de la clase persona y utiliza los métodos para 
mostrar los datos y calcular el año de nacimiento.
"""
import datetime

class Persona:
    def __init__(self, nombre, edad, genero, nacionalidad = "Mexico"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad

    def informacion(self):
        print("------Informacion------")
        print(f"{self.nombre} ({self.genero})")
        print(f"Edad: {self.edad} años")
        print(f"Nacionalidad: {self.nacionalidad}")

    def calcularNacimiento(self):
        year = datetime.date.today().year
        return year - self.edad
    
def main():
    objpersona = Persona("Eliab", 16, "Masculino")
    objpersona.informacion()
    print(f"Año de nacimiento: {objpersona.calcularNacimiento()}")

if __name__ == "__main__":
    main()

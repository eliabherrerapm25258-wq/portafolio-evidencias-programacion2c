class Ave:
    def __init__(self, color = "verde"):
        self.color = color

    def volar(self):
        print("Puedo volar")
        
class canario(Ave):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def informacion(self):
        pass

canario = canario("fulanito")
canario.color = "amarillo"
print(canario.color)
canario.volar()
print(canario.color)
class cafeteria:
    def preparar_cafe(self):
        self.__hervir_agua()
        self.__moler_cafe()
        print("cafe preparado")
        
    def __hervir_agua(self):
        print("hervir agua")
        
    def __moler_cafe(self):
        print("moler cafe")
        
def main():
    cafetera = cafeteria()
    cafetera.preparar_cafe()

if __name__ == "__main__":
    main()
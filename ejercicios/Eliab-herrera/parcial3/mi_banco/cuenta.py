class cuenta:
    """
<<<<<<< HEAD
    Presetacion de una cuenta bancaria
    
    Atributos:
        cliente: nombre del cliente.
        cuenta: numero de cuenta.
        saldo: saldo actual de la cuenta."""

    
    def __init__(self, cliente, cuenta, saldo = 0):
        """
        Inicializa una nueva cuenta bancaria.
        
        Args:
            cliente: nombre del cliente.
            cuenta: numero de cuenta.
            saldo: saldo inicial de la cuenta. (por defecto 0)
        """
=======
Representacion de una cuenta bancaria
 
    Atributos:
        cliente: nombre del cliente.
        cuenta: numero de cuenta.
        saldo: saldo actual de la cuenta. (por defecto 0)
     """
    
    def __init__(self, cliente, cuenta, saldo = 0):
      """ 
Inicializa una nueva cuenta bancaria.
 
     Agrs:
        cliente: nombre del cliente.
        cuenta: numero de cuenta.
        saldo: saldo inicial de la cuenta. (por defecto 0)
       """
>>>>>>> bd8b18700bd22324d798791328037410e72b65c7
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo

    def deposito(self, cantidad):
        """
<<<<<<< HEAD
        Realiza un deposito en la cuenta.

        Args:
            cantidad:(float) ingresa la cantidad a depositar. Debe ser un valor positivo.

        Returns:
            bool:True si el deposito fue exitoso.
            bool:False si la cantidad es negativa.
=======
Realiza un deposito en la cuenta.
   
        Agrs:
            cantidad:(float) ingresa la cantidad a depositar. Debe ser un valor positivo.
        Returns:
            bool: True si el deposito fue exitoso.
            bool: False si la cantidad es negativa.
>>>>>>> bd8b18700bd22324d798791328037410e72b65c7

        """
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False
    
    def retiro(self,cantidad):
        """
<<<<<<< HEAD
        Realiza un retiro de la cuenta.
        
        Args:
            cantidad:(float) ingresa la cantidad a retirar
        
        Returns:
            bool:True si el retiro fue exitoso.
            bool:false si el saldo es isuficiente o si la cantidad es cero.
        """
=======
Realiza un retiro de la cuenta.
        Agrs:
            cantidad:(float) ingresa la cantidad a retirar
        Returns:
            bool: True si el retiro fue exitoso.
            bool: False si el saldo es isuficiente o si la cantidad es cero.
          """
>>>>>>> bd8b18700bd22324d798791328037410e72b65c7
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
    
def main():
    pass

if __name__ == "__main__":
    main()

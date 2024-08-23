# Definimos la clase DispositivoElectronico que representa un dispositivo electrónico
class DispositivoElectronico:
    # Método inicializador de la clase
    def __init__(self):
        # Solicitamos al usuario que ingrese el tipo de dispositivo
        self.tipo = input("Ingrese el tipo de dispositivo (Celular/Tablet/Portátil): ")
        # Solicitamos al usuario que ingrese el modelo del dispositivo
        self.modelo = input("Ingrese el modelo del dispositivo: ")
        # Solicitamos al usuario que ingrese la capacidad del dispositivo
        self.capacidad = input("Ingrese la capacidad del dispositivo (e.g., 128GB, 8GB RAM): ")
        # Solicitamos al usuario que ingrese el color del dispositivo
        self.color = input("Ingrese el color del dispositivo: ")
        # Solicitamos al usuario que ingrese el tamaño de la pantalla
        self.pantalla = input("Ingrese el tamaño de la pantalla (e.g., 6.5 pulgadas): ")
        # Solicitamos al usuario que ingrese la capacidad de la batería
        self.bateria = input("Ingrese la capacidad de la batería (e.g., 4000mAh): ")
        # Solicitamos al usuario que ingrese el precio de compra del dispositivo
        self.precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))
        # Establecemos una marca predeterminada para el dispositivo
        self.marca = "PHR"  
        # Establecemos un origen predeterminado para el dispositivo
        self.origen = "Importado"  
        # Calculamos el precio de venta basado en el precio de compra
        self.precio_venta = self.calcular_precio_venta()

    # Método para calcular el precio de venta del dispositivo
    def calcular_precio_venta(self):
        # El precio de venta es el precio de compra multiplicado por un factor de 1.7
        return self.precio_compra * 1.7

    # Método para mostrar los datos del dispositivo
    def mostrar_datos(self):
        # Imprimimos la información del dispositivo
        print("\nCaracterísticas del dispositivo:")
        print(f"Tipo: {self.tipo}")
        print(f"Modelo: {self.modelo}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Color: {self.color}")
        print(f"Tamaño de Pantalla: {self.pantalla}")
        print(f"Capacidad de Batería: {self.bateria}")
        print(f"Marca: {self.marca}")
        print(f"Origen: {self.origen}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Registro del primer dispositivo
print("Registro del primer dispositivo:")
dispositivo1 = DispositivoElectronico()  # Creamos una instancia de la clase DispositivoElectronico
dispositivo1.mostrar_datos()  # Mostramos los datos del primer dispositivo

# Registro del segundo dispositivo
print("\nRegistro del segundo dispositivo:")
dispositivo2 = DispositivoElectronico()  # Creamos otra instancia de la clase DispositivoElectronico
dispositivo2.mostrar_datos()  # Mostramos los datos del segundo dispositivo

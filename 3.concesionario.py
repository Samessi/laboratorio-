# Definimos la clase Auto que representa un automóvil
class Auto:
    # Método inicializador de la clase
    def __init__(self):
        # Solicitamos al usuario que ingrese la marca del auto
        self.marca = input("Ingrese la marca del auto: ")
        # Solicitamos al usuario que ingrese el modelo del auto
        self.modelo = input("Ingrese el modelo del auto: ")
        # Solicitamos al usuario que ingrese el año del auto
        self.año = input("Ingrese el año del auto: ")
        # Solicitamos al usuario que ingrese el color del auto
        self.color = input("Ingrese el color del auto: ")
        # Solicitamos al usuario que ingrese el tipo de combustible
        self.tipo_combustible = input("Ingrese el tipo de combustible (Gasolina/Diesel/Eléctrico): ")
        # Solicitamos al usuario que ingrese el tipo de transmisión
        self.transmision = input("Ingrese el tipo de transmisión (Automática/Manual): ")
        # Solicitamos al usuario que ingrese el tipo de motor
        self.motor = input("Ingrese el tipo de motor (e.g., 2.0L): ")
        # Solicitamos al usuario que ingrese el origen del auto
        self.origen = input("Ingrese el origen del auto (Nacional/Importado): ")
        # Solicitamos al usuario que ingrese el precio de compra del auto
        self.precio_compra = float(input("Ingrese el precio de compra del auto: "))
        # Calculamos el precio de venta del auto basado en el precio de compra
        self.precio_venta = self.calcular_precio_venta()
        # Definimos el número de ruedas del auto (generalmente 4)
        self.ruedas = 4  
        # Definimos la capacidad de pasajeros del auto (típicamente 5)
        self.capacidad = 5  

    # Método para calcular el precio de venta del auto
    def calcular_precio_venta(self):
        # El precio de venta es el precio de compra multiplicado por un factor de 1.4
        return self.precio_compra * 1.4

    # Método para mostrar los datos del auto
    def mostrar_datos(self):
        # Imprimimos la información del auto
        print("\nCaracterísticas del vehículo:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Transmisión: {self.transmision}")
        print(f"Motor: {self.motor}")
        print(f"Origen: {self.origen}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Registro del primer auto
print("Registro del primer auto:")
auto1 = Auto()  # Creamos una instancia de la clase Auto
auto1.mostrar_datos()  # Mostramos los datos del primer auto

# Registro del segundo auto
print("\nRegistro del segundo auto:")
auto2 = Auto()  # Creamos otra instancia de la clase Auto
auto2.mostrar_datos()  # Mostramos los datos del segundo auto

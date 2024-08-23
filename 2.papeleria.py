class Papeleria:
    def __init__(self, cuadernos=0, lapices=0, precio_compra=0):
        # Inicializa los atributos del artículo en papelería
        self.cuadernos = cuadernos
        self.lapices = lapices
        self.marca_cuadernos = "Hojitas"  # Marca predeterminada de cuadernos
        self.marca_lapices = "Rayas"     # Marca predeterminada de lápices
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()  # Calcula el precio de venta basado en el precio de compra

    def calcular_precio_venta(self):
        # Calcula el precio de venta aplicando un margen del 30% sobre el precio de compra
        return self.precio_compra * 1.30

    def recibir_datos(self):
        # Solicita datos al usuario para actualizar los atributos del artículo
        tipo_cuaderno = int(input("Seleccione el tipo de cuaderno (1: 50 Hojas, 2: 100 Hojas): "))
        if tipo_cuaderno == 1:
            self.cuadernos = "100 Hojas"
        elif tipo_cuaderno == 2:
            self.cuadernos = "100 Hojas"
        else:
            print("Opción no válida.")
        
        tipo_lapiz = input("Seleccione el tipo de lápiz (grafito o color): ").lower()
        if tipo_lapiz == "grafito":
            self.lapices = "Lápiz de Grafito"
        elif tipo_lapiz == "color":
            self.lapices = "Lápiz de Color"
        else:
            print("Opción no válida.")
        
        self.precio_compra = float(input("Ingrese el precio de compra: "))
        self.precio_venta = self.calcular_precio_venta()  # Recalcula el precio de venta basado en el nuevo precio de compra

    def mostrar_datos(self):
        # Muestra todos los detalles del artículo
        print("\nDetalles del artículo registrado:")
        print(f"Marca de Cuadernos: {self.marca_cuadernos}")
        print(f"Tipo de Cuaderno: {self.cuadernos}")
        print(f"Marca de Lápices: {self.marca_lapices}")
        print(f"Tipo de Lápiz: {self.lapices}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Crear y procesar el primer artículo
articulo1 = Papeleria()
articulo1.recibir_datos()  # Solicita datos del usuario para el primer artículo
articulo1.mostrar_datos()  # Muestra los detalles del primer artículo

# Crear y procesar el segundo artículo
articulo2 = Papeleria()
articulo2.recibir_datos()  # Solicita datos del usuario para el segundo artículo
articulo2.mostrar_datos()  # Muestra los detalles del segundo artículo

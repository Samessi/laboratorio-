class ClinicaVeterinaria:
    def __init__(self, peso=0, nombre_mascota="", raza="", color_pelo="", edad_mascota=0, sexo=""):
        # Inicializa los atributos de la instancia y establece el estado inicial
        self.estado_atencion = "SIN ATENDER"
        self.peso = peso
        self.tamano = self.calcular_tamano()  # Determina el tamaño basado en el peso inicial
        self.nombre_mascota = nombre_mascota
        self.raza = raza
        self.color_pelo = color_pelo
        self.edad_mascota = edad_mascota
        self.sexo = sexo

    def calcular_tamano(self):
        # Calcula el tamaño del perro basado en su peso
        if self.peso <= 12:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def actualizar_estado(self):
        # Cambia el estado de atención a "ATENDIDO" y lo devuelve
        self.estado_atencion = "ATENDIDO"
        return self.estado_atencion

    def ingresar_datos(self):
        # Solicita datos al usuario para actualizar los atributos del perro
        self.nombre_mascota = input("Nombre de la Mascota: ")
        self.raza = input("¿Qué raza es su mascota?: ")
        self.color_pelo = input("Color del pelaje de su mascota: ")
        self.edad_mascota = int(input("Edad de su mascota (en años): "))
        self.peso = int(input("Peso de su mascota (en kg): "))
        self.sexo = input("Sexo de su mascota: ")
        self.tamano = self.calcular_tamano()  # Recalcula el tamaño basado en el peso ingresado

    def mostrar_datos(self):
        # Muestra todos los detalles del perro
        print(f"Nombre: {self.nombre_mascota}")
        print(f"Raza: {self.raza}")
        print(f"Color del pelaje: {self.color_pelo}")
        print(f"Edad: {self.edad_mascota} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Sexo: {self.sexo}")
        print(f"Estado: {self.estado_atencion}")

# Crear una instancia de ClinicaVeterinaria
mascota = ClinicaVeterinaria()  
# Ingresar los datos del perro
mascota.ingresar_datos()  
# Cambiar el estado de atención a "ATENDIDO"
mascota.actualizar_estado()  
# Mostrar todos los datos del perro
mascota.mostrar_datos()
